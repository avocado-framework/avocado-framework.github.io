---
layout: utils
---

# Utility Libraries

<table id="utils-table">
  <thead>
  <tr class="header">
  <th>Name/Description</th>
  <th>Category</th>
  <th>Maintainer</th>
  <th>Supported Platforms</th>
  <th>tests</th>
  <th>remote</th>
  </tr>
  </thead>

  <tbody>
  {% for util_dir_hash in site.data.autils %}
      {% assign util_dir = util_dir_hash[1] %}
      {% for util_hash in util_dir %}
          {% assign util = util_hash[1] %}
          <tr>
          <td>
                <strong markdown="spawn">{{util.name}}</strong>
                <p markdown="spawn">{{util.description}}</p>
          </td>
          <td>
                <ul>
                {% for category in util.categories %}
                   <li markdown="span">{{category}}</li>
                {% endfor %}
                </ul>
          </td>
          <td>
                <ul>
                {% for maintainer in util.maintainers %}
                   <li markdown="span">{{maintainer["name"]}}, {{maintainer["email"]}}</li>
                {% endfor %}
                </ul>
          </td>
          <td>
                <ul>
                {% for platform in util.supported_platforms %}
                   <li markdown="span">{{platform}}</li>
                {% endfor %}
                </ul>
          </td>
          <td>
                <ul>
                {% for test in util.tests %}
                   <li markdown="span">{{test}}</li>
                {% endfor %}
                </ul>
          </td>
          <td markdown="span">{{util.remote}}</td>
          </tr>
      {% endfor %}
  {% endfor %}
  </tbody>
</table>


