ci: deps lint test

deps:
	pip install -r requirements.txt

lint:
	ansible-playbook --syntax-check -i localhost, --connection=local test/test.yml

test:
	ansible-playbook --sudo -i localhost, --connection=local test/test.yml

.PHONY: ci deps lint test
