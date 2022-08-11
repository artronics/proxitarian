from invoke import task


@task
def build(c, docs=False):
    c.run("echo yarooo")
