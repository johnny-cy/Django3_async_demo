from django.shortcuts import render
from django.http import HttpResponse
import time
from asgiref.sync import sync_to_async
import asyncio
from myapp.models import Movie
# Create your views here.


# help func
@sync_to_async
def get_movie_async(x):
    if x == "a":
        print("preparing to get A...")
        for i in range(1000000):
            qa = Movie.objects.all()
        print("A is ready.")
    else:
        print("Preparing to get B...")
        for i in range(1000000):
            qa = Movie.objects.all()
        print("B is ready.")

def get_movie_sync(x):
    if x == "a":
        print("preparing to get A...")
        for i in range(1000000):
            qa = Movie.objects.all()
        print("A is ready.")
    else:
        print("Preparing to get B...")
        for i in range(1000000):
            qa = Movie.objects.all()
        print("B is ready.")

def home_view(request):
    return HttpResponse('<H2>Hello Django 3.1</H2>')

def main_view_sync(request):
    start_time = time.time()
    get_movie_sync("a")
    get_movie_sync("b")
    total = (time.time() - start_time )
    print("total = ", total)
    return HttpResponse(f"sync time: {total}")


async def main_view_async(request):
    start_time = time.time()
    task1 = asyncio.ensure_future(get_movie_async("a"))
    task2 = asyncio.ensure_future(get_movie_async("b"))
    # await asyncio.wait([task1, task2]) # wait till both tasks finished.
    # or doesn't wait and let it go straight to the end.
    total = (time.time() - start_time )
    print("total = ", total)
    return HttpResponse(f"Async time: {total}")


# ### What to know about these code ?
# browser -> localhost:8000/sync -> run main_view_sync will occupied terminal till finish. 
# output :
# preparing to get A...
# A is ready.
# Preparing to get B...
# B is ready.

# browser -> localhost:8000/async -> run main_view_async (has await) will occupied terminal till finish too.
# but both func run simulteniously
# preparing to get A...
# Preparing to get B...
# A is ready.
# B is ready.
 
#  browser -> localhost:8000/async -> run main_view_async ( no await ) will NOT occupied ternimal, but go straight to bottom
#  outcome will run detachedly. ( don't know how to receive the return, guess it might not own the thread anymore.)