from starlette.middleware.cors import CORSMiddleware
from supertokens_python import get_all_cors_headers
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe.thirdparty import ProviderInput, ProviderConfig, ProviderClientConfig
from supertokens_python.recipe import dashboard
from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import emailpassword, session, thirdparty

from api.api.v1 import expense
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine

from api.db.base import Base
from api.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(settings.database_url, echo=settings.debug, pool_pre_ping=True, future=True)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False, future=True)

    # Optional for dev; in prod use Alembic migrations instead
    Base.metadata.create_all(engine)

    app.state.engine = engine
    app.state.sessionmaker = SessionLocal
    try:
        yield
    finally:
        engine.dispose()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    redirect_slashes=False,
    lifespan=lifespan
)

init(
    app_info=InputAppInfo(
        app_name=settings.app_name,
        api_domain=settings.api_domain,
        website_domain=settings.website_domain,
        api_base_path="/auth",
        website_base_path="/auth"
    ),
    supertokens_config=SupertokensConfig(
        connection_uri=settings.supertokens_connection_uri,
        api_key=settings.supertokens_api_key
    ),
    framework='fastapi',
    recipe_list=[
	    session.init(),
        emailpassword.init(),
        dashboard.init(),
        thirdparty.init(
            sign_in_and_up_feature=thirdparty.SignInAndUpFeature(providers=[
                ProviderInput(
                    config=ProviderConfig(
                        third_party_id="google",
                        clients=[
                            ProviderClientConfig(
                                client_id=settings.google_client_id,
                                client_secret=settings.google_client_secret,
                            ),
                        ],
                    ),
                )
            ])
        )
    ],
    mode='asgi'
)

app.add_middleware(get_middleware())

app.include_router(expense.router, prefix="/api/v1/expense", tags=["accounts"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.website_domain
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)
