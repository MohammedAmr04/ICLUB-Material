# JavaScript Bootcamp (4 Sessions)

- **Level**: Beginner
- **Sessions**: 4
- **Final Project**: Products Manager — CRUD on top of a mock API layer
- **Previous Track**: [CSS + Tailwind Bootcamp](./02-css.md)
- **Next Track**: [React Bootcamp](./04-react.md)

------------------------------------------------------------------------

> **Core vs optional**: every topic under `## Topics` is required. Anything
> under `### Optional Extensions` is a bonus — it will not appear in the
> assessment unless stated otherwise.

## Prerequisites

-   Completed the [CSS + Tailwind Bootcamp](./02-css.md)
-   Can navigate a terminal, run a local server, and open DevTools
-   Git installed and configured

## Sessions

-   [Session 1 — Fundamentals & the Runtime](#session-1--fundamentals--the-runtime)
-   [Session 2 — Data, Scope & Storage](#session-2--data-scope--storage)
-   [Session 3 — Asynchronous JavaScript & the Data Layer](#session-3--asynchronous-javascript--the-data-layer)
-   [Session 4 — Debugging, Tooling & the Capstone](#session-4--debugging-tooling--the-capstone)
-   [Final Deliverables](#final-deliverables)
-   [Assessment](#assessment)

------------------------------------------------------------------------

# Session 1 — Fundamentals & the Runtime

**Duration**: 5 hours — **Goal**: write correct modern JavaScript and start a
real project from day one.

## Topics

### How JavaScript Runs

-   The engine, the runtime, and the difference between them
-   Parse, compile, execute
-   The call stack, the heap, and why the stack overflows
-   The browser vs Node.js: two hosts for the same language
-   The `console` beyond `log`: `table`, `group`, `count`, `time`, `assert`

### Values & Variables

-   `var`, `let`, `const` and when each is correct
-   Hoisting and the temporal dead zone
-   Primitive types vs reference types
-   Copy by value vs copy by reference
-   `typeof`, `null`, `undefined`, `NaN`
-   Type coercion and the `==` vs `===` trap
-   Truthy, falsy, and the falsy value list

### Operators & Control Flow

-   Arithmetic, assignment, and compound assignment
-   `&&`, `||`, `??` and the nullish coalescing use case
-   Optional chaining `?.`
-   Ternary and `switch`
-   `if` / `else` and early returns
-   `for`, `while`, `for...of`
-   `break`, `continue`

### Functions

-   Function declarations vs expressions
-   Parameters, default values
-   Return values and early returns
-   Arrow functions and the lexical `this`
-   Pure functions and side effects
-   IIFEs and why modules make them unnecessary

### Strings & Composition

-   Template literals, interpolation, multi-line strings
-   `length`, `includes`, `slice`, `split`, `trim`, `replace`, `replaceAll`
-   `padStart` / `padEnd`
-   When a template literal is the right output format

### Modules, Tooling & Git

-   ES Modules: `import` and `export`
-   Named exports vs default exports
-   Why you are using modules from day one
-   Vite: creating a JavaScript project and the dev server
-   `npm` scripts and `package.json`
-   `dependencies` vs `devDependencies`, and why the distinction matters
-   Semantic version ranges: `^`, `~`, `exact`, and `*`
-   `package-lock.json`, `npm ci`, and reproducible installs
-   `npx` for running a binary without installing it globally
-   What the build tool actually does: bundling, transpilation, targets,
    minification, HMR
-   Dev vs production builds and why `import.meta.env.DEV` matters
-   `.gitignore`
-   Folder structure: `components/`, `data/`, `services/`, `utils/`, `assets/`
-   `init`, `status`, `add`, `commit`, `log`
-   Branching, switching, merging, and a simple merge conflict

## Live Coding

-   Write a calculator from an empty file in fifteen minutes
-   Predict the output of ten hoisting and coercion snippets, then run them

## Homework

-   Calculator
-   Grade System
-   Multiplication Table

## Project Work

-   Initialize a Vite project with strict mode, add a `.gitignore`, and push
    the first commit
-   Create the folder structure the React track will reuse
-   Create `data/products.js` and `data/users.js` as ES modules of plain
    objects

------------------------------------------------------------------------

# Session 2 — Data, Scope & Storage

**Duration**: 5 hours — **Goal**: manipulate structured data immutably, control
state over time, and persist it safely.

## Topics

### Objects

-   Creating, reading, nesting, and deleting properties
-   Dot vs bracket notation and when bracket is required
-   Optional chaining and nullish assignment
-   `Object.keys`, `values`, `entries`
-   Shallow vs deep copy, and `structuredClone`
-   Structured copy, and when `structuredClone` beats a manual deep copy
-   `Object.freeze`
-   Spreading to update instead of mutating

### Arrays

-   `push`, `pop`, `shift`, `unshift`, `splice`, `slice`, `concat`
-   Mutating vs non-mutating methods
-   `length` and sparse arrays (brief)

### Map & Set

-   `Map` for keyed collections: any key type, insertion order, real
    `size`, and `has()`
-   Why an object literal is the wrong tool: key coercion, the
    `__proto__` footgun, and integer-like keys being reordered
-   `Set` for uniqueness, and `has` / `add` / `delete`
-   Converting between `Map`, `Set`, `Object`, and `Array`
-   `WeakMap` / `WeakSet` and why they are for object identity, not iteration
-   Deduplicating with `new Set(array)`

### Regular Expressions

-   Literal syntax `/.../` vs the `RegExp` constructor
-   Flags: `g`, `i`, `m`, `s`, `u`, `y` — and what each changes
-   Character classes `[a-z]`, negation `[^...]`, and escapes `\d \w \s`
-   Quantifiers `* + ? {n,m}` and lazy vs greedy matching
-   Anchors `^`, `$`, and word boundaries `\b`
-   Groups, capturing vs non-capturing `(?:...)`, and named groups
-   `test`, `exec`, `match`, `matchAll`, `replace`, `replaceAll`, `split`
-   The global flag's `lastIndex` statefulness trap
-   Practical recipes: email, phone, strong password, URL slug
-   When *not* to use a regex — never to parse HTML

### Iteration Methods

-   `map` and when it is the wrong tool
-   `filter`
-   `reduce` and writing an accumulator that makes sense
-   `find`, `findIndex`, `findLast`
-   `some`, `every`
-   `includes`
-   `flat`, `flatMap`
-   `sort` and the comparator, plus why the mutating version matters
-   `toSorted`, `toReversed`, `with` — the non-mutating ES2023 versions
-   Chaining methods and readability

### Destructuring & Rest

-   Object destructuring: renaming, defaults, nesting
-   Array destructuring and the swap idiom
-   Rest in destructuring vs rest in parameters
-   Spread in calls, arrays, and objects
-   Combining rest and spread in one signature

### Scope & Closures

-   Global, function, and block scope
-   Lexical scoping and scope chains
-   Closures: functions that remember their creation scope
-   Closures in loops and the classic `var` bug
-   Memory retention and cleaning up listeners
-   `this`: implicit, explicit, and lexical binding; `call` / `apply` / `bind`
    and why you will still meet them in dependencies
-   Dynamic `import()` and tree shaking

### Data Formats

-   `JSON.stringify` and `JSON.parse`
-   What JSON cannot represent: functions, `undefined`, `Date`, `Map`
-   Dates: `Date`, `toISOString`, and formatting
-   Numbers: `toFixed` vs `Intl.NumberFormat`, and float money

### Storage

-   `localStorage` and `sessionStorage`
-   The API is synchronous and string-only
-   Quota errors and `SecurityError` in private mode
-   JSON round-trips and what breaks on the way back
-   A `storage` wrapper with parsing, defaults, and error handling
-   When not to use storage: server state belongs on the server
-   `crypto.randomUUID()` for keys and ids that must stay stable
-   The `storage` event and syncing state across open tabs

### Browser APIs

-   `setTimeout`, `setInterval`, and always clearing them
-   `requestAnimationFrame` and the 16.7ms frame budget
-   `cancelAnimationFrame`
-   `IntersectionObserver` for "is it on screen" without scroll listeners
-   `ResizeObserver` for element size changes
-   `matchMedia` for media queries in JavaScript
-   `URL` and `URLSearchParams` for parsing, building, and reading query
    strings
-   `FormData` for form submissions, including `File` objects
-   `Blob`, `File`, and `URL.createObjectURL` for previews
-   `crypto.randomUUID()`

### Optional Extensions

-   Iterators, generators, and `Symbol.iterator`
-   `Symbol` and well-known symbols
-   `BigInt` and when a number genuinely is not a number
-   `Clipboard` API for copy buttons
-   `PerformanceObserver` for real user metrics
-   `BroadcastChannel` for cross-tab messaging
-   WebSockets and `EventSource` — when a request/response model is not enough
-   Service workers, and the caching layer they sit on
-   `structuredClone` limitations and the deep-clone library question

## Live Coding

-   Do CRUD on an array of products, then do it again without mutating
-   Build a closure-based counter and explain exactly what it captures
-   Write a storage wrapper and break it in three different ways

## Homework

-   **Immutable CRUD**: list, filter by category, compute totals, add and
    remove items — all without mutation
-   Closure Counter as a factory producing independent counters

## Project Work

-   Render product cards into the DOM with `map()` from the Session 1 data
-   Create `utils/helpers.js` with reusable pure functions
-   Create `utils/storage.js` with a safe localStorage wrapper
-   No DOM access inside the data or utility modules

------------------------------------------------------------------------

# Session 3 — Asynchronous JavaScript & the Data Layer

**Duration**: 6 hours — **Goal**: build a service layer the React track can
swap without rewriting a single component.

## Topics

### The Event Loop

-   Call stack, Web APIs, task queue, microtask queue
-   The order of execution and why it is not the order you wrote
-   Starvation and how it breaks the UI
-   `queueMicrotask` and observing the loop yourself

### Promises

-   Callback hell and what it caused
-   Promise states: pending, fulfilled, rejected
-   `.then`, `.catch`, `.finally`
-   Chaining and error propagation down a chain
-   Returning a promise vs a value inside `then`

### Combining Async Work

-   `Promise.all` and its fail-fast behaviour
-   `Promise.allSettled` and when partial results are better
-   `Promise.race` and `Promise.any`
-   Sequential vs parallel and the cost of a waterfall

### async / await

-   `async` and implicit promise wrapping
-   `await` and suspension
-   Error handling with `try` / `catch` / `finally`
-   Top-level `await`
-   Sequential awaits and the mistake they usually hide
-   Never mixing `.then` and `await` in one function

### fetch

-   `fetch`, `Request`, `Response`
-   Status codes: 2xx, 3xx, 4xx, 5xx
-   HTTP methods: GET, POST, PUT, PATCH, DELETE
-   Headers, `Content-Type`, and sending JSON
-   **`fetch` resolves on 4xx and 5xx** — the most common bug of the session
-   `response.json()` and its failure modes
-   Credentials and CORS concepts
-   Timeouts with `AbortSignal.timeout`
-   Cancelling with `AbortController`

### Errors

-   Errors as values vs thrown exceptions
-   `throw` and re-throwing
-   Custom error classes and `error instanceof`
-   `Error.cause`
-   Never swallowing an error silently
-   Validating input at the boundary
-   What to show the user vs what to log

### Rate-Limiting Input

-   Debounce: waiting for the user to stop typing
-   Throttle: acting at most once per interval
-   Which one a search box needs
-   Debouncing a request and cancelling the previous one

### The Service Layer

-   Separating data access from UI code
-   A stable interface so the implementation can change
-   A mock implementation with artificial latency and random failures
-   Normalizing and validating data leaving a service
-   Caching responses in storage
-   Abort signals flowing through the service signature

### Web Security Essentials

-   XSS: how untrusted data becomes executable code
-   `innerHTML` vs `textContent`, and why one is a vulnerability and the other
    is not
-   Sanitising user-generated HTML, and the cases where you should not accept
    it at all
-   Where to keep a token: `localStorage` vs an httpOnly cookie vs memory
-   The XSS-versus-CSRF tradeoff behind that choice
-   What CSRF is and what same-site cookies do about it
-   `rel="noopener noreferrer"` on any `target="_blank"` link
-   Why secrets in a browser bundle are public secrets
-   HTTPS, and what a mixed-content warning actually means

**Service contract — a hard deliverable; the React track depends on it:**

```text
getProducts({ search, category, page, limit, signal })  -> Promise<Product[]>
getProductById(id)                                       -> Promise<Product>
createProduct(payload)                                   -> Promise<Product>
updateProduct(id, payload)                               -> Promise<Product>
deleteProduct(id)                                        -> Promise<void>

getUsers({ search, status, page, limit, signal })        -> Promise<User[]>
updateUserStatus(id, status)                             -> Promise<User>

login({ email, password })                               -> Promise<{ token, user }>
logout()                                                 -> Promise<void>
getCurrentUser()                                         -> Promise<User | null>
```

## Live Coding

-   Predict the output order of a set of timers and promises, then run them
-   Build `getProducts` over a local array with simulated latency and an
    `AbortSignal`

## Homework

-   Fetch users from JSONPlaceholder and map them into your own user shape

## Project Work

-   **Mock API layer**: implement the contract above against a local array
    -   Artificial 300–800ms delay
    -   A ~10% failure rate switchable via an environment flag
    -   Search, category filter, and pagination done inside the service
    -   `signal` support so in-flight requests can be cancelled
    -   Validation that throws a typed error with a readable message
-   Wire the existing page to the service — zero data logic left in the view
-   Implement a loading state, an error state with retry, and an empty state

------------------------------------------------------------------------

# Session 4 — Debugging, Tooling & the Capstone

**Duration**: 6 hours — **Goal**: diagnose bugs from the error message, keep
the codebase clean automatically, and finish the project.

## Topics

### Reading Errors

-   Error types and what each one means
-   Stack traces and how to read them top-down
-   `TypeError: cannot read properties of undefined` and its three real causes
-   Reference vs Type vs Syntax errors
-   When a `ReferenceError` is a typo and when it is a scope bug

### DevTools

-   The debugger: breakpoints, step over, step into, step out
-   Conditional breakpoints and logpoints
-   Watch expressions
-   The Network tab: status, timing, payload, and copying a request as `curl`
-   Overrides and local overrides
-   The Performance panel: a quick flame-chart read
-   Memory: detached nodes and leaks

### Code Quality

-   ESLint: rules worth enabling and rules that are noise
-   Prettier for formatting
-   `npm run lint` and `npm run format`
-   Linting as a gate in Git
-   Naming, function length, and early returns
-   Comments that explain why, not what
-   Dead code and unused exports

### Configuration

-   `import.meta.env` and environment variables
-   `.env` files and `.env.example`
-   What must never be committed
-   Why a browser bundle cannot hide a secret
-   The `MOCK_FAILURE_RATE` flag the service reads

### Common Pitfalls

-   `==` and implicit coercion
-   Mutating a value you were given
-   Sharing one array reference across records
-   Using an object as a map
-   Forgetting `await`
-   Assuming async code runs in order
-   Float arithmetic with money
-   `NaN` propagation
-   A regex with the `g` flag reused across calls
-   Trusting client-side validation

### Testing

-   Why test, and what testing is *not*
-   Vitest: install, config, and `npm run test`
-   The anatomy of a test: arrange, act, assert
-   What to test: pure functions, services, and error paths
-   What not to test: implementation details and the framework itself
-   Using the mock API's latency and failure flags as your fixtures
-   Seeding `localStorage` for a test that needs it
-   Coverage reports and what they do not tell you
-   Red-green-refactor as the loop

### Optional Extensions

-   Test doubles: fakes, stubs, mocks, and when you need which
-   Snapshot testing, and why it usually creates noise instead of confidence
-   Property-based testing
-   Testing DOM code with a headless browser
-   CI: running the suite on every push

### Shipping the Capstone

-   Wire every screen to the service layer
-   Full CRUD, confirmed by the loading, error, and empty states
-   A README that explains how to run it

## Live Coding

-   Diagnose five broken scripts from the error message alone
-   Convert a messy file into Prettier-formatted, lint-clean code

## Homework

-   Find and fix ten seeded bugs, writing one sentence per fix about the root
    cause

## Project Work

-   **Products Manager — the track capstone**
    -   Product list with search, category filter, and pagination
    -   Create, edit, and delete, all through the service contract
    -   Every screen has a loading, error, and empty state
    -   Validation errors surfaced to the user
    -   State persisted with the `storage` wrapper
    -   ESLint passes, Prettier formatted, clean Git history on a real branch
    -   A README with run instructions and the architecture in one diagram
-   A test suite covering the services, the error paths, and at least one
    forced-failure case

------------------------------------------------------------------------

# Final Deliverables

-   Calculator, Grade System, Multiplication Table (Session 1)
-   Immutable CRUD and a storage wrapper (Session 2)
-   **Mock API layer implementing the full service contract (Session 3)**
-   **Products Manager — the capstone (Session 4)**

## Assessment

-   **Correctness**: features work, and the error, loading, and empty states
    are implemented — not just the happy path
-   **Immutability**: no mutation of arguments or shared state
-   **Architecture**: zero data access in the view layer; the service interface
    survives an implementation swap unchanged
-   **Robustness**: typed errors, no silent `catch`, input validated at the
    boundary
-   **Security**: no `innerHTML` on untrusted data, and a stated reason for where
    the token lives
-   **Tests**: the service layer and at least one failure path are covered
-   **Quality**: ESLint clean, Prettier formatted, meaningful commit history on
    a branch
-   **Submission**: pushed to a Git repository with a README
