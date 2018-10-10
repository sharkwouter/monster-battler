DIAGRAMS= diagrams/gameflow.uml
createUML: $(DIAGRAMS)
	@plantuml $(DIAGRAMS)
