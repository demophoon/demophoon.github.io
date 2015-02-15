Title: Jenkins Job Builder
Date: 2015-02-15T11:35-08:00
Tags: Technology, Python, Jenkins, Automation, CI
Slug: jenkins-job-builder
Authors: Britt Gresham

So this weekend I spent some time playing around with [Jenkins Job
Builder](https://github.com/openstack-infra/jenkins-job-builder) by Openstack
and I'm a massive fan. I have not started using jenkins in my personal life
until now and all I want to do is add jenkins to everything since discovering
this.

What JJB lets you do is write out basic job configurations in a Yaml file and
when you run `jenkins-jobs update ./path/to/jobs.yaml` it generates jenkins
configs and uploads them to your jenkins server. This lets you manage your
jenkins instance in a way that can be versioned and auditable! Big win there!
You can also specify templates in the yaml files and use the templates as bases
for jobs. I'm starting to do this with my python projects by first creating a
template for doing PEP-8 checks on code, as well as a template for running any
tests I create, and putting all of those individual jobs into a job group. You
can think of job groups as mini pipelines. After I have created that pipeline
adding new python projects turns from hours of cloning and modifying jobs in
Jenkins into just modifying your job configurations to utilize that job group.

When you update the jobs all of the mini jobs in a pipeline are created
automagically and kept up to date with what is in the configurations. I don't
even see why you'd need to run the update command if that itself is a Jenkins
job!

If you are interested in seeing my configurations they are all open and
available here: [https://github.com/demophoon/jenkins-jobs](https://github.com/demophoon/jenkins-jobs)

This blog post was published using Jenkins!
