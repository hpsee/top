# TOP

Digital Records for High Performance Computing

![assets/images/code-logo.png](assets/images/code-logo.png)

>Every HPC Center wants to have the biggest and baddest clusters. While the 
[TOP500](https://www.top500.org/) holds official status for international centers, 
this leaves out smaller groups that want to participate, and doesn't encompass 
all the kinds of records that might be obtained. Welcome, reader, to the
Digital Book of World Records for HPC. [Visit the site](https://hpcee.github.io/top/) to learn more, or
continue reading for how to contribute to this repository.

## Frequently Asked Questions

### How does it work?

Each post in [_posts](_posts) corresponds to one record. For each, we define
a title, and the creation and updated at date (same as the creation date, if the
record is newly added):

```
---
title:  "Largest number of jobs in Queue"
date:   2019-06-12 12:00:00 -0400
updated: 2019-06-12 12:00:00 -0400
categories: record slurm largest
---
```

In the content area, we write a description of the record, followed by a section
for each winner. We have three different levels of winners:

 - academic institution
 - national lab
 - corporate entity

This means that each record can have a maximum of three winners, and a section 
for each. For examples, see the files in the posts folder.


### Can I contribute a new record?

Yes! Each record is a post under [_posts](_posts) and you can simply copy
any post to use as a template, and rename with the date and a name for
the record. You can open a pull request to [https://www.github.com/hpcee/top](https://www.github.com/hpcee/top)
to discuss your contribution.


### Can I update a record?

Competition is good! If you see a record that your center has surpassed, it's up
to you to fix the historical record! You should also open a pull request
to edit the page in question. The previous winners will be remembered
via version control.

If you have any other questions, please don't hesitate to ask by
[opening an issue](https://www.github.com/hpcee/top/issues).
