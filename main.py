import time
import luigi


class HelloTask(luigi.Task):

    param = luigi.Parameter()

    def run(self):
        with self.output().open('w') as f:
            f.write(self.param)

    def output(self):
        return luigi.LocalTarget('/tmp/hello-%s.txt' % self.param)


class HelloWorldTask(luigi.Task):

    def requires(self):
        return HelloTask('world')

    def run(self):
        time.sleep(10*60)
        with self.output().open('w') as f:
            f.write('Hello there!')

    def output(self):
        return luigi.LocalTarget('/tmp/hello.txt')


if __name__ == '__main__':
    luigi.run()
