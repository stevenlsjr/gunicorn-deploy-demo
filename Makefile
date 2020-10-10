

.PHONY: buildx all clean

TAGFLAGS:=stevenlsjr/gunicorn-demo:latest \
	stevenlsjr/gunicorn-demo:0.0

PLATFORMS:=linux/amd64,linux/arm64

BUILDFLAGS:=$(TAGFLAGS:%=-t %) \
	--platform $(PLATFORMS) \
	--push

all: buildx

buildx:
	docker buildx build . $(BUILDFLAGS)