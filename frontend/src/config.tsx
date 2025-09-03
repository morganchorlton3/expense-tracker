import EmailPassword from 'supertokens-auth-react/recipe/emailpassword';
import { EmailPasswordPreBuiltUI } from 'supertokens-auth-react/recipe/emailpassword/prebuiltui';
import ThirdParty, {
  Google,
  Github,
  Apple,
  Twitter,
} from 'supertokens-auth-react/recipe/thirdparty';
import { ThirdPartyPreBuiltUI } from 'supertokens-auth-react/recipe/thirdparty/prebuiltui';
import Session from 'supertokens-auth-react/recipe/session';

export function getApiDomain() {
  const apiPort = 8000;
  const apiUrl = `http://localhost:${apiPort}`;
  return apiUrl;
}

export function getWebsiteDomain() {
  const websitePort = 3000;
  const websiteUrl = `http://localhost:${websitePort}`;
  return websiteUrl;
}

export const SuperTokensConfig = {
  appInfo: {
    appName: 'SuperTokens Demo App',
    apiDomain: getApiDomain(),
    websiteDomain: getWebsiteDomain(),
    apiBasePath: '/auth',
    websiteBasePath: '/auth',
  },

  recipeList: [
    EmailPassword.init(),
    ThirdParty.init({
      signInAndUpFeature: {
        providers: [Google.init(), Github.init(), Apple.init()],
      },
    }),
    Session.init(),
  ],
  getRedirectionURL: async (context: { action: string; newSessionCreated: boolean }) => {
    if (context.action === 'SUCCESS' && context.newSessionCreated) {
      return '/dashboard';
    }
  },
};

export const recipeDetails = {
  docsLink: 'https://supertokens.com/docs/quickstart/introduction',
};

export const PreBuiltUIList = [EmailPasswordPreBuiltUI, ThirdPartyPreBuiltUI];

export const ComponentWrapper = (props: { children: JSX.Element }): JSX.Element => {
  return props.children;
};
