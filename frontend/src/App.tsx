import SuperTokens, { SuperTokensWrapper } from 'supertokens-auth-react';
import { getSuperTokensRoutesForReactRouterDom } from 'supertokens-auth-react/ui';
import { SessionAuth } from 'supertokens-auth-react/recipe/session';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import * as ReactRouter from 'react-router-dom';
import Dashboard from './Dashboard';
import { PreBuiltUIList, SuperTokensConfig, ComponentWrapper } from './config';
import Home from './Home';

// Initialize SuperTokens - ideally in the global scope
SuperTokens.init(SuperTokensConfig);

function App() {
  return (
    <SuperTokensWrapper>
      <BrowserRouter>
        <main className="App app-container">
          <div className="fill" id="home-container">
            <ComponentWrapper>
              <Routes>
                <Route path="/" element={<Home />} />
                {/* This shows the login UI on "/auth" route */}
                {getSuperTokensRoutesForReactRouterDom(ReactRouter, PreBuiltUIList)}

                {/* This protects the "/dashboard" route so that it shows
                                <Dashboard /> only if the user is logged in.
                                Else it redirects the user to "/auth" */}
                <Route
                  path="/dashboard"
                  element={
                    <SessionAuth>
                      <Dashboard />
                    </SessionAuth>
                  }
                />
              </Routes>
            </ComponentWrapper>
          </div>
        </main>
      </BrowserRouter>
    </SuperTokensWrapper>
  );
}

export default App;
