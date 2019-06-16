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


### The Centers Map

The top site includes a [map](https://hpsee.github.io/top/map/) of academic,
national lab, and company centers. The data comes from [centers.yml](_data/centers.yml),
where each entry corresponds to a cluster resource:

```yaml
-
    name: 'Lawrence Berkeley National Laboratory'
    id: lbnl-lawrencium
    external_url: 'http://scs.lbl.gov/'
    resource_name: Lawrencium
    size_nodes: ""
    size_cores: '30,000'
    purpose: 'General institution HPC resource'
    notes: ""
    coords: [37.876036, -122.250078]
```

If you want to add a new record, we suggest that you first ensure that
the center or resource is included in this data. If you find it, you
can provide a link that opens up on the map based on the center id. For
example, to link to the entry above we would use "lbnl-lawrencium" and
the link would open at `{{ site.baseurl }}/map/?q=lbnl-lawrencium`

#### Adding a New Center

The metadata is fairly straight forward, and minimally you should provide
a unique id (all lowercase and not already used, this will be tested), an 
external url, and coordinates for the map. And of course, if you see any 
issue with current metadata, please open an issue or pull request to fix it.


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
