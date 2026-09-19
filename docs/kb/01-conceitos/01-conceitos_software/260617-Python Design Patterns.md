[Web](https://python-patterns.guide/)

[[260617_conceitos_info]]

I’m **Brandon Rhodes** ([website](https://rhodesmill.org/brandon/), [Twitter](https://twitter.com/brandon_rhodes)) and this is my evolving guide to design patterns in the [Python programming language](https://www.python.org/).

- This site is letting me collect my ideas about Python and Design Patterns all in one place.
- My hope is that these pages make the patterns more discoverable — easier to find in web searches, and easier to read — than when they were scattered across the videos and slides of my [Python conference talks](http://rhodesmill.org/brandon/talks/).
- The weight of other obligations makes my progress intermittent. To check for new material, simply visit the commit history of this site’s [project repository on GitHub](https://github.com/brandon-rhodes/python-patterns), where you can also select “Watch” to get updates.

With those preliminaries complete, here are the patterns!

# 1. Gang of Four: Principles

- [The Composition Over Inheritance Principle](https://python-patterns.guide/gang-of-four/composition-over-inheritance/)
	- [Problem: the subclass explosion](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#problem-the-subclass-explosion)
		- [Solution #1: The Adapter Pattern](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#solution-1-the-adapter-pattern)
		- [Solution #2: The Bridge Pattern](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#solution-2-the-bridge-pattern)
		- [Solution #3: The Decorator Pattern](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#solution-3-the-decorator-pattern)
		- [Solution #4: Beyond the Gang of Four patterns](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#solution-4-beyond-the-gang-of-four-patterns)
		- [Dodge: “if” statements](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-if-statements)
		- [Dodge: Multiple Inheritance](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-multiple-inheritance)
		- [Dodge: Mixins](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-mixins)
		- [Dodge: Building classes dynamically](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-building-classes-dynamically)

# 2. Python-Specific Patterns

- [The Global Object Pattern](https://python-patterns.guide/python/module-globals/)
	- [The Constant Pattern](https://python-patterns.guide/python/module-globals/#the-constant-pattern)
		- [Import-time computation](https://python-patterns.guide/python/module-globals/#import-time-computation)
		- [Dunder Constants](https://python-patterns.guide/python/module-globals/#dunder-constants)
		- [The Global Object Pattern](https://python-patterns.guide/python/module-globals/#id1)
		- [Global Objects that are mutable](https://python-patterns.guide/python/module-globals/#global-objects-that-are-mutable)
		- [Import-time I/O](https://python-patterns.guide/python/module-globals/#import-time-i-o)
- [The Prebound Method Pattern](https://python-patterns.guide/python/prebound-methods/)
	- [Alternatives](https://python-patterns.guide/python/prebound-methods/#alternatives)
		- [The pattern](https://python-patterns.guide/python/prebound-methods/#the-pattern)
- [The Sentinel Object Pattern](https://python-patterns.guide/python/sentinel-object/)
	- [Sentinel Value](https://python-patterns.guide/python/sentinel-object/#sentinel-value)
		- [The Null Pointer Pattern](https://python-patterns.guide/python/sentinel-object/#the-null-pointer-pattern)
		- [The Null Object Pattern](https://python-patterns.guide/python/sentinel-object/#the-null-object-pattern)
		- [Sentinel Objects](https://python-patterns.guide/python/sentinel-object/#sentinel-objects)

# 3. Gang of Four: Creational Patterns

- [The Abstract Factory Pattern](https://python-patterns.guide/gang-of-four/abstract-factory/)
	- [The Pythonic approach: callable factories](https://python-patterns.guide/gang-of-four/abstract-factory/#the-pythonic-approach-callable-factories)
		- [Restriction: outlaw passing callables](https://python-patterns.guide/gang-of-four/abstract-factory/#restriction-outlaw-passing-callables)
		- [Restriction: outlaw passing classes](https://python-patterns.guide/gang-of-four/abstract-factory/#restriction-outlaw-passing-classes)
		- [Generalizing: the complete Abstract Factory](https://python-patterns.guide/gang-of-four/abstract-factory/#generalizing-the-complete-abstract-factory)
- [The Builder Pattern](https://python-patterns.guide/gang-of-four/builder/)
	- [The Builder as convenience](https://python-patterns.guide/gang-of-four/builder/#the-builder-as-convenience)
		- [Nuance](https://python-patterns.guide/gang-of-four/builder/#nuance)
		- [Dueling builders](https://python-patterns.guide/gang-of-four/builder/#dueling-builders)
		- [A degenerate case: simulating optional arguments](https://python-patterns.guide/gang-of-four/builder/#a-degenerate-case-simulating-optional-arguments)
- [The Factory Method Pattern](https://python-patterns.guide/gang-of-four/factory-method/)
	- [Dodge: use Dependency Injection](https://python-patterns.guide/gang-of-four/factory-method/#dodge-use-dependency-injection)
		- [Instead: use a Class Attribute Factory](https://python-patterns.guide/gang-of-four/factory-method/#instead-use-a-class-attribute-factory)
		- [Instead: use an Instance Attribute Factory](https://python-patterns.guide/gang-of-four/factory-method/#instead-use-an-instance-attribute-factory)
		- [Instance attributes override class attributes](https://python-patterns.guide/gang-of-four/factory-method/#instance-attributes-override-class-attributes)
		- [Any callables accepted](https://python-patterns.guide/gang-of-four/factory-method/#any-callables-accepted)
		- [Implementing](https://python-patterns.guide/gang-of-four/factory-method/#implementing)
- [The Prototype Pattern](https://python-patterns.guide/gang-of-four/prototype/)
	- [The problem](https://python-patterns.guide/gang-of-four/prototype/#the-problem)
		- [Pythonic solutions](https://python-patterns.guide/gang-of-four/prototype/#pythonic-solutions)
		- [Implementing](https://python-patterns.guide/gang-of-four/prototype/#implementing)
- [The Singleton Pattern](https://python-patterns.guide/gang-of-four/singleton/)
	- [Disambiguation](https://python-patterns.guide/gang-of-four/singleton/#disambiguation)
		- [The Gang of Four’s implementation](https://python-patterns.guide/gang-of-four/singleton/#the-gang-of-fours-implementation)
		- [A more Pythonic implementation](https://python-patterns.guide/gang-of-four/singleton/#a-more-pythonic-implementation)
		- [Verdict](https://python-patterns.guide/gang-of-four/singleton/#verdict)

# 4. Gang of Four: Structural Patterns

- [The Composite Pattern](https://python-patterns.guide/gang-of-four/composite/)
	- [Example: the UNIX file system](https://python-patterns.guide/gang-of-four/composite/#example-the-unix-file-system)
		- [On hierarchies](https://python-patterns.guide/gang-of-four/composite/#on-hierarchies)
		- [Example: GUI programming with Tkinter](https://python-patterns.guide/gang-of-four/composite/#example-gui-programming-with-tkinter)
		- [Implementation: to inherit, or not?](https://python-patterns.guide/gang-of-four/composite/#implementation-to-inherit-or-not)
- [The Decorator Pattern](https://python-patterns.guide/gang-of-four/decorator-pattern/)
- [The Flyweight Pattern](https://python-patterns.guide/gang-of-four/flyweight/)