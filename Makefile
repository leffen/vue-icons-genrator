APP= vueicongen
DOCKER_REPO=leffen

DOCKER_IMAGE= $(DOCKER_REPO)/$(APP)

bump:
	bumper -f VERSION  -p p

build:
	docker build  -t $(DOCKER_IMAGE):$(shell cat VERSION) .

push:
	docker push  $(DOCKER_IMAGE):$(shell cat VERSION)

release: bump buildd
	docker push  $(DOCKER_IMAGE):$(shell cat VERSION)