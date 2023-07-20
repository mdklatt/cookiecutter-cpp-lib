# Project management tasks; see CMakeLists.txt for building the project.

BUILD_TYPE = Debug
BUILD_ROOT = build/$(BUILD_TYPE)
VENV = .venv
PYTHON = . $(VENV)/bin/activate && python


$(VENV)/.make-update: requirements-dev.txt
	python -m venv $(VENV)
	$(PYTHON) -m pip install -U pip  # needs to be updated first
	$(PYTHON) -m pip install -r $^
	touch $@


.PHONY: dev
dev: $(VENV)/.make-update
	cmake -DCMAKE_BUILD_TYPE=$(BUILD_TYPE) -DBUILD_TESTING=ON -DBUILD_DOCS=ON -S . -B $(BUILD_ROOT)


.PHONY: build
build:
	cmake --build $(BUILD_ROOT)


.PHONY: test
test: build
	. $(VENV)/bin/activate
	cd $(BUILD_ROOT) && ctest


.PHONY: docs
docs:
	cmake --build $(BUILD_ROOT) --target docs
