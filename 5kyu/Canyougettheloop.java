import java.util.*;
public class LoopInspector {

  public int loopSize(Node node) {
    final Set<Node> result = new LinkedHashSet<>();
    while(result.add(node)) { //filling result
      node = node.getNext();
    }
    final Iterator<Node> iterator = result.iterator();
    for (int i = 0;; i++) { //looking for the cycle
      if (iterator.next() == node) {
        return result.size() - i;
      }
    }
  }
}
