pipi:
	@echo "Installing pip dependencies..."
	@pip install -r requirements.txt

specdl:
	@echo "Downloading OpenAPI spec..."
	# @curl -O https://api.modelmetry.com/sdk/spec.yaml
	@curl -O http://0.0.0.0:8888/sdk/spec.yaml

specgen:
	@echo "Generating OpenAPI spec..."
	@npx @openapitools/openapi-generator-cli generate \
		-i spec.yaml \
		-g python \
		-o . \
		--additional-properties=packageName=modelmetry.openapi,generateSourceCodeOnly=true

t:
	@echo "Running tests (with Pytest)..."
	@pytest -v -s