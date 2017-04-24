const _registry = {
  decorators: {},
  sources: {},
  strategies: {},
};

const registerDecorator = (name, decorator) => {
  _registry.decorators[name] = decorator;
  console.log('decorator: ' + name);
};

const getDecorator = (name) => {
  return _registry.decorators[name];
};

const registerSource = (name, source) => {
  _registry.sources[name] = source;
  console.log('source: ' + name);
};

const getSource = (name) => {
  return _registry.sources[name];
};

const registerStrategy = (name, strategy) => {
  _registry.strategies[name] = strategy;
  console.log('strategy: ' + name);
};

const getStrategy = (name) => {
  return _registry.strategies[name];
};

export {
  registerDecorator,
  getDecorator,
  registerSource,
  getSource,
  registerStrategy,
  getStrategy,
}
