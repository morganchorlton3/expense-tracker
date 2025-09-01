from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import emailpassword, session

from api.core.config import settings

init(
    app_info=InputAppInfo(
        app_name=settings.app_name,
        api_domain=settings.api_domain,
        website_domain=settings.website_domain,
        api_base_path="/auth",
        website_base_path="/auth"
    ),
    supertokens_config=SupertokensConfig(
        connection_uri="https://st-dev-1c03bc70-876c-11f0-8a81-2b90616abe4c.aws.supertokens.io",
        api_key='eSPWDt3PYhEpeg3alcUpE5e-ED'
    ),
    framework='fastapi',
    recipe_list=[
	    session.init(),
        emailpassword.init()
    ],
    mode='asgi'
)