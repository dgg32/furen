creator "Sixing Huang"
version "2"
graph [
	node [
		$id "2e7ctj"
		tags "Drug"
		$map 0
		$path "$"
		*label "drug_cui"
	]
	node [
		$id "ctjaxr"
		tags "MOA"
		$map 0
		$path "$"
		*label "moa_id"
	]
	edge [
		$source "2e7ctj"
		$target "ctjaxr"
		label "HAS_MOA"
		$single 1
	]
]