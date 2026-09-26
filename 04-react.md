# React Bootcamp (7 Sessions)

- **Level**: Intermediate
- **Sessions**: 7
- **Final Project**: AdminHub — a multi-page admin dashboard
- **Previous Track**: [JavaScript Bootcamp](./03-javascript.md)

------------------------------------------------------------------------

## Prerequisites

-   Completed the [JavaScript Bootcamp](./03-javascript.md)
-   Comfortable with ES Modules, Promises, `async`/`await`, and `fetch`
-   The service contract from JavaScript Session 3 is implemented and working
-   Fluent in utility classes, either from Tailwind or your own design system
-   Git, Node.js, and a code editor are set up

## Sessions

-   [Session 1 — Fundamentals & State](#session-1--fundamentals--state)
-   [Session 2 — Effects & Data Fetching](#session-2--effects--data-fetching)
-   [Session 3 — Composition, Custom Hooks & Context](#session-3--composition-custom-hooks--context)
-   [Session 4 — Routing & App Structure](#session-4--routing--app-structure)
-   [Session 5 — Forms & Validation](#session-5--forms--validation)
-   [Session 6 — Server State & the API Layer](#session-6--server-state--the-api-layer)
-   [Session 7 — Performance, Accessibility & Deployment](#session-7--performance-accessibility--deployment)
-   [Final Deliverables](#final-deliverables)
-   [Assessment](#assessment)

> **Core vs optional**: every topic under `## Topics` is required. Anything
> under `### Optional Extensions` is a bonus — it will not appear in the
> assessment unless stated otherwise.

> Session 1 merges React basics and state management, so it is the longest
> session at roughly 7 hours. If you need to split it, break after "Lists" and
> before "State".

------------------------------------------------------------------------

# Session 1 — Fundamentals & State

**Duration**: 7 hours — **Goal**: think in components, and make the UI
interactive with the right state in the right place.

## Topics

### Setup

-   Creating a Vite + React project
-   The dev server, HMR, and the React DevTools extension
-   Why Vite's default folder structure is not enough for a real app
-   `npm run` scripts: dev, build, preview, lint

### JSX

-   What JSX compiles to
-   The rules: one root, tags must close, camelCase attributes
-   Fragments `<>...</>` and why they matter for lists and flex layout
-   Conditional rendering: ternary vs `&&` and the `0` trap
-   Rendering nothing with `null` / `false`
-   Styling with the Tailwind utilities from the previous track
-   Importing assets and SVGs

### Components

-   Function components and the naming convention
-   Props and destructuring with defaults
-   `children` and container components
-   One-way data flow
-   Composition vs configuration with props

### Lists

-   Rendering arrays with `map`
-   Keys: why `index` is a last resort
-   Keys and reconciliation
-   Fragment keys when you need a wrapper
-   Stable ids from the data, not from the array position

### Refs & Escape Hatches

-   `useRef` for a value that survives re-renders without causing one
-   Reading and writing the DOM through a ref
-   Focusing an input on mount — the case a state variable cannot do
-   Storing the previous value of a prop
-   Why a ref is not state, and what breaks if you treat it as state
-   `useId` for accessible `id` / `htmlFor` / `aria-describedby` pairs
-   `createPortal` for rendering outside the parent's DOM subtree
-   Why a modal must be portalled: overflow, stacking contexts, and `z-index`
-   The rules of refs: do not read or write a ref during render

### State

-   `useState` and why a component needs its own memory
-   The render cycle: a state change triggers a re-render
-   State is a snapshot, not a variable
-   Functional updates and why they are required
-   Batching and stale closures
-   State updates must be immutable
-   Rules of hooks: top level, consistent order, never conditional

### Events

-   Handlers, event objects, and the synthetic event wrapper
-   Inline vs defined handlers and the re-creation cost
-   Passing arguments to a handler
-   Form events and `preventDefault`
-   `stopPropagation` and when it is a workaround, not a fix

### Controlled Inputs

-   Controlled vs uncontrolled
-   Binding an input to state
-   Deriving state from other state
-   The controlled/uncontrolled warning and what causes it
-   Handling checkboxes, radios, and selects
-   `key` to reset a form after submission

### Lifting State Up

-   Lifting to the closest common ancestor
-   When to lift and when not to
-   The single source of truth principle
-   Collocating state instead of centralising everything

### useReducer

-   When `useState` becomes unwieldy
-   Actions, reducer, and dispatch
-   Actions as a plain-language log
-   Reducers as pure, testable functions
-   State shape design and avoiding impossible states

### Persistence

-   Persisting state with the `storage` wrapper from the JavaScript track
-   Reading the initial value lazily
-   A theme toggle that survives a refresh
-   Why server data must not be persisted this way

### Staying Responsive

-   `useTransition` for non-urgent updates
-   `useDeferredValue` for a value that is allowed to lag behind
-   Both as answers to: the search box feels laggy on a long list
-   What transitions do not do: they are not debouncing, and they are not a
    substitute for server pagination

### Rendering Safely

-   `dangerouslySetInnerHTML` and what it is actually saying
-   The one legitimate use (a sanitised rich-text field) and the rule that
    comes with it
-   Why "the data came from our own API" is not a security argument
-   Where sanitisation belongs

## Live Coding

-   Build a static dashboard layout — sidebar, navbar, three stat cards — with
    no state at all
-   Build a controlled form, then explain what happens if the state is removed
-   Convert a `useState` counter into a `useReducer` and compare readability

## Homework

-   Reusable Product Card: a presentational component with no internal state
-   Todo App: add, edit, complete, delete, filter, and persist to storage

## Project Work

-   **AdminHub shell**
    -   Navbar, Sidebar, and Dashboard layout composed from small components
    -   Fake data imported as a module
    -   Product search, category filter, and a persisted theme toggle
    -   Product list and user list rendered from state

------------------------------------------------------------------------

# Session 2 — Effects & Data Fetching

**Duration**: 5 hours — **Goal**: synchronise with the outside world and stop
fighting the dependency array.

## Topics

### The Render Cycle

-   Render, commit, and the browser paint
-   What React does and what the browser does
-   When an effect runs

### useEffect

-   The basic shape: `useEffect(fn, deps)`
-   The dependency array and referential identity
-   Cleanup and why it is mandatory, not optional
-   Effects that synchronise with external systems — and effects that only
    derive state
-   Strict Mode double-invocation and why it is a feature
-   `useLayoutEffect` and the one case it is for
-   `useInsertionEffect` (mention only)

### Common Mistakes

-   Missing dependencies
-   Objects and arrays as dependencies
-   Effect dependency loops
-   State that should be derived instead
-   Effects as a substitute for event handlers
-   Data fetching in an effect at all — a preview of Session 6

### Fetching Data

-   A `useFetch` custom hook: loading, error, data, retry
-   Cancellation on unmount
-   Race conditions and `AbortController`
-   Debounced search requests with cancellation
-   Handling the three states properly: loading, error, empty
-   Retry with backoff
-   Caching in memory so a re-mount does not refetch

### UI States

-   Skeleton loaders that match the final layout
-   Spinners and when they are the wrong choice
-   Empty states with a real next action
-   Error states that are recoverable
-   Optimistic feedback and how to revert it

## Live Coding

-   Write a `useFetch` hook, then break it three ways: no cleanup, a missing
    dependency, no cancellation
-   Implement a debounced search that cancels the previous request

## Homework

-   Search Users using the service layer, with cancellation and an error state

## Project Work

-   **Dashboard statistics** fetched from the service
    -   Four stat cards, each with its own loading skeleton and error state
    -   A **Recent Activity** section fed by its own hook
    -   Stable keys and an empty state on the activity list
-   Every screen reports loading, error, and empty — not just the happy path

------------------------------------------------------------------------

# Session 3 — Composition, Custom Hooks & Context

**Duration**: 5 hours — **Goal**: structure the app so nothing repeats and no
component reaches across the tree.

## Topics

### Composition

-   Composition over inheritance
-   Children and render props
-   Compound components with shared context
-   Slots with named props
-   Headless components: behaviour without styling
-   Configurability vs a component per variation

### Custom Hooks

-   The rules of hooks apply to custom hooks too
-   `use` naming and why the linter enforces it
-   Designing a hook: inputs in, outputs out, no rendering
-   Reuse vs abstraction — the point of no return
-   Returning a tuple vs a named object
-   Hooks that compose other hooks

### Hooks to Build

-   `useLocalStorage` — with quota safety
-   `useDebounce`
-   `useToggle`
-   `useClickOutside`
-   `useOnEscape` and `useMediaQuery`
-   `usePagination`
-   `useAuth` (a stub returning a hard-coded user)

### Context API

-   The prop drilling problem, shown concretely
-   `createContext` and `useContext`
-   Splitting contexts to limit re-renders
-   Provider composition and nesting
-   Context for cross-cutting state, not for everything
-   Context is not a state manager, and when you outgrow it

### Architecture

-   Feature-based folder structure
-   Separating `components/`, `hooks/`, `services/`, and `lib/`
-   Barrel files and their cost
-   Where shared UI components live
-   Import direction rules and enforcing them with ESLint
-   Dependency injection by props instead of importing singletons

## Live Coding

-   Extract the theme logic used twice in Session 1 into one hook
-   Replace a five-level prop chain with a single context

## Homework

-   Convert repeated logic into at least three custom hooks, each with JSDoc
    describing its inputs and outputs

## Project Work

-   **Refactor AdminHub**
    -   Every repeated effect moved into a custom hook
    -   Theme state into a `ThemeProvider`
    -   Auth state into an `AuthProvider` backed by the `useAuth` stub
    -   `Button`, `Input`, `Card`, `Modal`, `Table`, and `Badge` extracted as
        shared components with Tailwind variants
    -   The `Modal` portalled, with a focus trap, `Escape` to close, and focus
        restored to the trigger on close
    -   An ESLint rule blocking deep imports across feature boundaries

------------------------------------------------------------------------

# Session 4 — Routing & App Structure

**Duration**: 5 hours — **Goal**: turn the app into a real multi-page
application with working navigation and guards.

## Topics

### Routing Concepts

-   Client-side routing vs server routing
-   The History API: push, replace, popstate
-   What a router actually does
-   URL as state and why it matters

### React Router

-   `createBrowserRouter` and the data router model
-   `<RouterProvider>`
-   Route objects: `path`, `element`, `children`, `index`
-   Layout routes and `<Outlet>`
-   `Link` vs `NavLink` and active styles
-   `useNavigate`, `useParams`, `useSearchParams`, `useLocation`
-   `useMatch` and route matching patterns
-   Splat routes

### Structure

-   Nested routes and shared layouts
-   A root layout, an authenticated layout, and a dashboard layout
-   Index routes and redirect routes
-   404 handling and catch-all routes
-   Error boundaries per route

### Protected Routes

-   Redirecting unauthenticated users
-   Preserving the intended destination after login
-   The auth check must not cause a flash of protected content
-   Role-based guards (mention)
-   Why a guard is a UX feature, not security

### The Session Lifecycle

This is the part a real login flow lives or dies on, and it is invisible in a
happy-path demo.

-   Access token vs refresh token, and why there are two
-   Token expiry and what a 401 actually means
-   A single-flight refresh: queue the failed requests, refresh once, then
    replay
-   Where the refresh happens so no component has to think about it
-   Logout: clearing local state, revoking the refresh token, and cancelling
    in-flight requests
-   Logging out every device, and why a server-side revocation list exists
-   403 vs 401: authenticated but not allowed
-   The CSRF angle of using cookies instead of headers
-   Choosing storage deliberately, and writing down why

### Optional Extensions

-   Role and permission checks at the route level
-   Remember-me and the long-lived session vs the short-lived token
-   Multi-tab auth sync
-   Route loaders and actions for auth-dependent data

### Code Splitting

-   `lazy` and `Suspense`
-   Route-level splitting
-   Avoiding a waterfall of chunks
-   A loading fallback and an error fallback

## Live Coding

-   Build a nested layout with an outlet and a 404 route in ten minutes
-   Implement a guard and explain the flash-of-content problem

## Homework

-   A small multi-page app with three nested routes and a protected page

## Project Work

-   **AdminHub routing**
    -   `/login`
    -   `/` → redirect to `/dashboard`
    -   `/dashboard` — stats, charts placeholder, recent activity
    -   `/products` — list, search, filter, pagination
    -   `/products/:id` — product details
    -   `/users` — list, search, status filter
    -   `/settings` — profile and theme
    -   `*` — a 404 page
-   All authenticated routes behind a guard
-   Route-level code splitting with a suspense fallback
-   Pagination and filters reflected in the URL, not only in state

------------------------------------------------------------------------

# Session 5 — Forms & Validation

**Duration**: 5 hours — **Goal**: build forms that are pleasant, validated
consistently, and accessible.

## Topics

### Form Strategy

-   Controlled, uncontrolled, and when each is correct
-   Why hand-rolling large forms does not scale
-   React Hook Form: registration, validation schema, touched state
-   Zod schemas and inferred types
-   One schema reused for the form, the API payload, and the response check
-   Sync vs async validation; validating on blur vs on submit

### Validation UX

-   Field-level vs form-level errors
-   Inline messages that are announced, not just coloured
-   Disabling submit and why it hides the reason it is disabled
-   Server-side validation errors mapped back to fields
-   Prefilled values and dirty tracking
-   Unsaved-changes protection

### Advanced

-   Multi-step forms and sharing state between steps
-   Array fields with `useFieldArray`
-   Dynamic add/remove rows
-   File uploads and previews
-   Optimistic updates with rollback when validation fails
-   `defaultValue` and reset semantics

### React 19's Native Answer

React now ships a form story of its own. You are allowed to prefer a library —
but you must be able to explain what the platform does instead.

-   `<form action={fn}>` and form actions
-   `useActionState` for the submit lifecycle and result
-   `useFormStatus` and why it needs a *child* component
-   `useOptimistic` for showing a value before the server confirms it
-   What React 19 did not change: you still validate on the server
-   When to use React Hook Form, when to use React 19, and when to use both
-   Progressive enhancement and the no-JavaScript question

### Optional Extensions

-   `use()` for reading a promise during render
-   Actions and the pending state as a first-class concept
-   Streaming a suspense boundary around a form
-   Multi-step forms with URL-driven state
-   Rich-text fields and the sanitiser you will need

### Accessibility

-   Every field has a real `<label>`, wired with `useId`
-   Error text linked with `aria-describedby`
-   `aria-invalid` and focus management on submit
-   Moving focus to the first invalid field with a ref
-   Submitting with `Enter` from any field
-   Never relying on placeholder or colour alone
-   Modals as dialogs: `role="dialog"`, `aria-modal`, labelled by their title
-   `inert` on the rest of the page while a dialog is open
-   Focus trap, `Escape` to close, and focus returned to the trigger
-   Announcing async results: `aria-live="polite"` for a status,
    `role="alert"` for an error
-   `aria-busy` on a region that is loading

## Live Coding

-   Build a product form with Zod and React Hook Form, including async
    uniqueness validation
-   Make a broken form accessible and justify every change

## Homework

-   Registration Form: schema-driven, accessible, with password rules and a
    confirmation match

## Project Work

-   **Product form work**
    -   Create product — full validation
    -   Edit product — prefilled, dirty tracking, cancel confirmation
    -   Delete product — an in-app confirm dialog, not a browser `confirm()`
    -   Service validation errors mapped back to the right field
    -   Accessible: labels, error announcements, focus management

------------------------------------------------------------------------

# Session 6 — Server State & the API Layer

**Duration**: 6 hours — **Goal**: stop hand-rolling caching, synchronisation,
and loading states.

## Topics

### Server State vs Client State

-   What lives on the server and why duplicating it is a bug
-   The three problems manual fetching creates: duplication, staleness, races
-   When `useState` + `useEffect` is genuinely enough
-   Introducing a library when the cost is real

### TanStack Query

-   Server state as a cache
-   `useQuery`: `queryKey`, `queryFn`, and the returned state
-   Query keys as a dependency system
-   `staleTime` vs `gcTime`, and why the defaults confuse people
-   `enabled` for dependent queries
-   Placeholder and initial data
-   `refetchInterval` and background refetching
-   Devtools for inspecting the cache

### Mutations

-   `useMutation` and its lifecycle
-   `onSuccess` / `onError` / `onSettled`
-   Cache invalidation with `queryClient.invalidateQueries`
-   Targeted updates with `setQueryData`
-   Optimistic updates and rollback
-   Preventing duplicate submissions

### Loading & Error UX

-   `isLoading`, `isFetching`, `isPending`, and the difference
-   Skeletons that mirror the final layout
-   Error boundaries vs query error states
-   Retry with exponential backoff
-   Empty states and zero-data UX
-   Global error handling and toast notifications

### The Service Layer

-   Why `fetch` is enough, and where a library would actually help
-   Axios and interceptors, and whether you still need them
-   Timeouts and cancellation in the service signature
-   Normalizing and validating responses
-   **The payoff**: swap the mock implementation from JavaScript Session 3 for a
    real backend with zero component changes

### Optional Extensions

-   `useSyncExternalStore` for reading a store outside React
-   Charts on the dashboard, with loading, empty, and error states
-   Infinite queries and cursor pagination
-   Normalised caches: merging one entity from several responses
-   Optimistic updates with `useOptimistic` instead of the cache
-   Offline support and mutation queues

### Opt-in Libraries

-   Why `fetch` is usually enough, and where a client adds real value
-   Axios, interceptors, and the case for a single client module
-   Retrying and backoff at the client layer
-   Auth headers and where a refresh interceptor belongs
-   Normalizing and validating responses at the boundary
-   A shared error type so the UI never parses a string

## Live Coding

-   Replace a hand-rolled `useEffect` fetch with `useQuery` and diff the line
    count
-   Implement an optimistic delete with rollback

## Homework

-   Full CRUD against a public API with TanStack Query, including invalidation

## Project Work

-   **Replace the fake services with the API layer**
    -   `queryKey` conventions documented in the code
    -   Mutations for create, update, and delete with invalidation
    -   Optimistic updates on the products list
    -   Loading skeletons, empty states, and error states on every page
    -   Search wired with `useQuery` + debounce + `enabled`
    -   The service interface from JavaScript Session 3 unchanged

------------------------------------------------------------------------

# Session 7 — Performance, Accessibility & Deployment

**Duration**: 6 hours — **Goal**: measure before optimising, cover the gaps, and
ship it.

## Topics

### Performance

-   The React DevTools Profiler and the commit timeline
-   What causes re-renders: props, context, state placement
-   `React.memo` and when it is not the answer
-   `useMemo` and `useCallback` — for expensive work and referential stability,
    not for micro-optimisation
-   Stabilising props passed to memoised children
-   Splitting context so unrelated consumers do not re-render
-   Virtualisation for long lists
-   Lazy loading images and heavy components
-   Reading a build report and knowing what is in the bundle
-   **Core Web Vitals**: LCP, CLS, INP, and TTFB — what each measures and
    which React mistake causes it
-   Measuring with Lighthouse and with real user monitoring
-   Fonts and layout shift: the two things that wreck LCP and CLS
-   Long tasks and INP: why a slow `onChange` handler is a performance bug

### Correctness & Resilience

-   Error boundaries and where to place them
-   `Suspense` boundaries
-   Recovering from a crash instead of showing a white page
-   Handling a slow or flaky connection

### Accessibility Pass

-   Semantic HTML before ARIA
-   Keyboard navigation and focus management for modals and menus
-   Visible focus styles
-   Live regions for async results and toasts
-   Contrast in both themes
-   Testing with the accessibility tree and a screen reader
-   **The RTL requirement**: `dir="rtl"`, logical properties
    (`margin-inline`, `padding-inline`, `inset-inline`), and icon mirroring

### Shipping

-   Environment variables per environment and `.env.example`
-   Production build and local preview
-   Deployment to a static host
-   Custom domain and HTTPS
-   SPA routing rewrites — the 404-on-refresh problem
-   Caching and asset versioning
-   Source maps in production
-   Basic error reporting
-   A README that explains how to run the project

### Testing

-   Vitest plus React Testing Library, and why Testing Library queries the
    rendered output instead of your internals
-   `getByRole` over `getByTestId`, and what that buys you
-   Testing a component's behaviour, not its state variables
-   Testing a custom hook with `renderHook`
-   A fresh `QueryClient` per test and why a shared cache leaks between tests
-   Mocking at the service boundary, not at the network layer
-   `user-event` for realistic interaction sequences
-   Testing the error and empty states — they are the ones that break silently
-   Coverage on the hooks and services, not on the presentational components
-   `npm test` in the deploy checklist

### Optional Extensions

-   MSW, or reusing the JavaScript track's mock API as the test double
-   Visual regression tests
-   E2E with Playwright for the login and checkout flows
-   The React Compiler, and what it changes about `memo` and `useMemo`

## Live Coding

-   Record a Profiler trace, find the expensive render, and fix it with the
    least code that works
-   Ship the app, break a deep link on refresh, and fix the rewrite rule

## Homework

-   Deploy the project and share the live URL

## Project Work

-   **Final polish**
    -   A performance pass with before/after Profiler evidence
    -   A responsive pass at 320px, 768px, 1024px, and 1440px
    -   Loading skeletons everywhere
    -   Empty states and error pages, not blank screens
    -   An accessibility pass, including a working keyboard path
    -   Deployed, with a README

------------------------------------------------------------------------

# Final Deliverables

-   AdminHub — a multi-page admin dashboard, deployed
-   **Authentication**: login, logout, protected routes, and a preserved
    destination after login
-   **Dashboard**: statistics cards, recent activity, charts
-   **Products**: list, search, filter, pagination, create, edit, delete
-   **Users**: list, search, status filter, status change
-   **Settings**: profile and theme
-   **Architecture**: feature-based folders, custom hooks, a service layer with
    a swappable implementation, and an ESLint import boundary
-   **Quality**: loading skeletons, empty states, error pages, an accessibility
    pass, and a performance pass with evidence

## Assessment

-   **Correctness**: every feature works, including the error, empty, and slow
    paths
-   **Architecture**: components never call the service directly; state lives at
    the right level; no prop drilling; no duplicated server state
-   **Data**: one query-key convention, correct invalidation, no hand-rolled
    cache
-   **Forms**: schema-driven, accessible, server errors mapped to fields
-   **UX**: skeletons that match the layout, actionable empty and error states
-   **Performance**: no unmeasured "optimisations"; Profiler evidence for every
    change that was made; a Lighthouse run before and after
-   **Auth**: a 401 triggers one refresh and a replay, not a redirect to login
-   **Security**: no `dangerouslySetInnerHTML` on untrusted data, and a written
    reason for the token storage choice
-   **Tests**: hooks, services, and every error state are covered
-   **Accessibility**: keyboard navigable, labelled, dialogs are dialogs,
    async results are announced, RTL-ready
-   **Shipped**: deployed, with a README and a clean lint pass

## Bonus

-   Dark mode driven by Tailwind theme variables and a persisted preference
-   Charts with a real library and their own empty states
-   Notifications with a toast system, an unread badge, and a live region
-   Role-based permissions, not just an auth guard
-   Localisation with more than one language, and a real RTL pass
-   Virtualised tables for large datasets

------------------------------------------------------------------------

# What Next

This track stops at plain React. The next three steps, in the order most teams
need them:

1. **TypeScript** — the single highest-leverage upgrade. Start by typing the
   service layer and the props of your shared components; the rest follows.
2. **A meta-framework** — Next.js, Remix, or React Router v7 in framework mode,
   for SSR, data loading, and the file-based routing you do not build yourself.
3. **Server Components** — a different rendering model, and the reason some of
   the client-state advice above stops applying.

Also worth knowing but not required: micro-frontends, WebAssembly, and native
mobile with React Native.
