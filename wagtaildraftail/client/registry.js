const registry = {
  decorators: {},
  sources: {},
  strategies: {},
};

const registerDecorator = (name, decorator) => {
  registry.decorators[name] = decorator;
};

const getDecorator = name => registry.decorators[name];

const registerSource = (name, source) => {
  registry.sources[name] = source;
};

const getSource = name => registry.sources[name];

const registerStrategy = (name, strategy) => {
  registry.strategies[name] = strategy;
};

const getStrategy = name => registry.strategies[name];

export {
  registerDecorator,
  getDecorator,
  registerSource,
  getSource,
  registerStrategy,
  getStrategy,
}
