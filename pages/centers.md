---
layout: page
title: Centers and Resources
permalink: /centers/
---


<table id="t01">
  <tr>
    <th></th>
    <th>Name</th>
    <th>Resource</th> 
    <th>Purpose</th>
    <th>Map</th>
    <th>Metrics</th>
  </tr>
{% for entry in site.data.centers %}<tr>
    <td>{{ forloop.index }}.</td>
    <td>{{ entry.name }}</td>
    <td><a href='{{ entry.external_url }}'>{{ entry.resource_name }}</a></td> 
    <td>{{ entry.purpose }}</td>
    <td><a href="{{ site.baseurl }}/map/?q={{ entry.id }}">View</a></td>
    <td>{% if entry.size_nodes != "" %}Nodes:{{ entry.size_nodes }}{% endif %} {% if entry.size_cores != "" %}Cores:{{ entry.size_cores }}{% endif %}</td>
</tr>{% endfor %}
</table>

Don't see your center or resource here? [Add it to the list](https://www.github.com/hpsee/top).
