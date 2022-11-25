clotho, one of the three Fates, spins the thread of the lives of all mortals
and decides when a person is born or dies.
this demo is inspired by https://github.com/burke/zeus

if you have a python project with many dependencies and slow startup time,
iterating on your code can be tedious.
you can fix this by first importing slow dependencies, forking,
and then importing frequently-changed code.
when some code changes, the parent (which has slow dependencies imported
but not your changed code) forks again and your project is "reloaded"

1. run `./reloader.py` and wait 5 seconds for `slow_lib` to get imported
2. curl `localhost:8000`
3. change `fast_lib`
4. curl `localhost:8000` again
5. rejoice
