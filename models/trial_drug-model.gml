creator "Sixing Huang"
version "2"
graph [
	node [
		$id "vydb2o"
		tags "Trial"
		$map 0
		$path "$"
		*label "PostingID"
	]
	node [
		$id "d4rex7"
		tags "Drug"
		$map 0
		$path "$"
		*label "drug_cui"
	]
	edge [
		$source "vydb2o"
		$target "d4rex7"
		label "TESTS"
		$single 1
	]
]