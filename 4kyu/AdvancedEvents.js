function Event() {
  let handlers = [];

    this.subscribe = function() {
        for (let i = 0; i < arguments.length; i++) {
            if (typeof arguments[i] == "function")
                handlers.push(arguments[i]);
        }
    };

    this.unsubscribe = function() {
        for (let i = 0; i < arguments.length; i++) {
            let j = handlers.lastIndexOf(arguments[i]);
            if (j >= 0)
                handlers.splice(j, 1);
        }
    };

    this.emit = function() {
        var invoke = handlers.slice();
        while (invoke.length)
            invoke.shift().apply(this, arguments);
    };
}
