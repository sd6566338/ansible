{% for i in All_server_list %}
object Host "M2-A{{ i.cabinet_number }}-{{ i.cabinet_begin }}U-{{ i.sn }}" {
	import "generic-host"
	address = "{{ i.manager_ip }}"
	vars.type = "m2-a-hp"
	vars.type2 = "hp"
}

{% endfor %}

