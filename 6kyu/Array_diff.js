function arrayDiff(a, b) {
	return a.filter(iter => b.indexOf(iter) == -1);
}
