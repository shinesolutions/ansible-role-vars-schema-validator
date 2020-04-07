ci: deps lint test

deps:
	pip install -r requirements.txt

lint:
	# yamllint examples/*.yaml tasks/*.yml
	ansible-playbook --syntax-check -i localhost, --connection=local test/playbook.yml

test:
	ansible-playbook --sudo -i localhost, --connection=local test/playbook.yml

.PHONY: ci deps lint test
