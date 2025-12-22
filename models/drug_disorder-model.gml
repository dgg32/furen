creator "Sixing Huang"
version "2"
graph [
	node [
		$id "30ot2l"
		tags "Drug"
		$map 0
		$path "$"
		*label "drug_cui"
	]
	node [
		$id "xl2eoq"
		tags "Disorder"
		$map 0
		$path "$"
		*label "disorder_cui"
	]
	edge [
		$source "30ot2l"
		$target "xl2eoq"
		label "MAY_TREAT"
		$single 1
	]
]