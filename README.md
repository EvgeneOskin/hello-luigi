# Hello luigi

This project is `Hello world`-like project on [luigi](https://github.com/spotify/luigi).

## Feature

The project provide the single feature. It writes files `/tmp/hello.txt` and `/tmp/hello-world.txt`.


## Install

Use [pipenv](https://github.com/kennethreitz/pipenv).

```bash
$ pipenv install
# Installing dependencies from Pipfile.lock (b72d65)…
```

## Run

Run it with `luigi` command.

```bash
$ luigid --background # Run luigi as a deamon
# Defaulting to basic logging; consider specifying logging_conf_file in luigi.cfg.
# 2017-12-05 00:19:34,892 luigi.scheduler[20120] INFO: No prior state file exists at /var/lib/luigi-server/state.pickle. Starting with empty state
# 2017-12-05 00:19:34,896 luigi.server[20120] INFO: Scheduler starting up
$ python main.py HelloWorldTask  # Run tasks
# DEBUG: Checking if HelloWorldTask() is complete
# DEBUG: Checking if HelloTask(param=world) is complete
# INFO: Informed scheduler that task   HelloWorldTask__99914b932b   has status   PENDING
# INFO: Informed scheduler that task   HelloTask_world_82a8b4cc97   has status   PENDING
# INFO: Done scheduling tasks
# INFO: Running Worker with 1 processes
# DEBUG: Asking scheduler for work...
# DEBUG: Pending tasks: 2
```

```bash
$ python main.py --local-scheduler HelloWorldTask  # Execute the task locally
# DEBUG: Checking if HelloWorldTask() is complete
# DEBUG: Checking if HelloTask(param=world) is complete
# INFO: Informed scheduler that task   HelloWorldTask__99914b932b   has status   PENDING
# INFO: Informed scheduler that task   HelloTask_world_82a8b4cc97   has status   DONE
# INFO: Done scheduling tasks
# INFO: Running Worker with 1 processes
# DEBUG: Asking scheduler for work...
# DEBUG: Pending tasks: 1
```
