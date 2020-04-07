ci: clean deps lint test

clean:
	rm -rf stage

stage:
	mkdir -p stage/roles/vars_schema_validator
	cp -R library/ stage/roles/vars_schema_validator/
	cp -R meta/ stage/roles/vars_schema_validator/
	cp -R tasks/ stage/roles/vars_schema_validator/

deps:
	pip install -r requirements.txt

lint: stage
	pylint library/*.py
	yamllint meta/*.y*ml tasks/*.y*ml test/*/*.y*ml
	ANSIBLE_ROLES_PATH=stage/roles/ ansible-playbook --syntax-check -i localhost, --connection=local test/*/playbook.yml

test: stage
	ANSIBLE_ROLES_PATH=stage/roles/ ansible-playbook -i localhost, --connection=local test/success/playbook.yml
	# TODO: check exit code of failure test case below
	ANSIBLE_ROLES_PATH=stage/roles/ ansible-playbook -i localhost, --connection=local test/failure/playbook.yml || echo "Failure test exit code $$?"

release:
	rtk release

.PHONY: ci clean stage deps lint test release
