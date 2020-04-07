ci: clean deps lint test

clean:
	rm -rf stage

init:
	mkdir -p stage/roles/vars_schema_validator

deps:
	pip install -r requirements.txt

lint:
	# yamllint examples/*.yaml tasks/*.yml
	ansible-playbook --syntax-check -i localhost, --connection=local test/playbook.yml

test: init
	cp -R library/ stage/roles/vars_schema_validator/
	cp -R meta/ stage/roles/vars_schema_validator/
	cp -R tasks/ stage/roles/vars_schema_validator/
	ANSIBLE_ROLES_PATH=stage/roles/ ansible-playbook -i localhost, --connection=local test/playbook.yml

.PHONY: ci clean init deps lint test
