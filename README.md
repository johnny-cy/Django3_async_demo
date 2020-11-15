# Django3_async_demo

## What to know about these code ?

browser -> localhost:8000/sync -> run main_view_sync will occupied terminal till finish.

OUTPUT1: 

preparing to get A...

A is ready.

Preparing to get B...

B is ready.

browser -> localhost:8000/async -> run main_view_async (has await) will occupied terminal till finish too.
but both func run simulteniously

OUTPUT2: 

preparing to get A...

Preparing to get B...

A is ready.

B is ready.
 
browser -> localhost:8000/async -> run main_view_async ( no await ) will NOT occupied ternimal, but go straight to bottom
outcome will run detachedly. ( don't know how to receive the return, guess it might not own the thread anymore.)

OUTPUT: 
same as OUTPUT2
