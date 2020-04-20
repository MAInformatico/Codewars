function arrayPlusArray(arr1, arr2) {
  return [...arr1, ...arr2].reduce((it1,it2) => it1+it2);
}
