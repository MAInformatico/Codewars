function CurryIt(func) {
  
  let ListArgs = [];
  let context = null;
  
  return function curry(...value) {
            if (this != ((function () {return this;}).call(null))) context = this;
    
            if (!value.length) {
              let retVal = func.call(context,...ListArgs);
              ListArgs = [];
              return retVal;
            }
            ListArgs = ListArgs.concat(value);
            return curry;
        }
  }
