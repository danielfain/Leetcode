import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {

    private Node<Item> first;
    private Node<Item> last;
    int count;

    class Node<Item> {
        Item item;
        Node<Item> next;
        Node<Item> prev;
    }

    public static void main(String[] args) {
        Deque<Integer> d = new Deque<>();
        d.addFirst(5);
        d.addLast(10);

        for (Integer i : d) {
            System.out.println(i);
        }
    }

    @Override
    public Iterator<Item> iterator() {
        return new Iterator<Item>() {
            @Override
            public boolean hasNext() {
                return !isEmpty();
            }

            @Override
            public Item next() {
                return removeFirst();
            }

            @Override
            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }

    // construct an empty deque
    public Deque() {
        first = new Node<>();
        last = new Node<>();
    }

    // is the deque empty?
    public boolean isEmpty() {
        return count == 0;
    }

    // return the number of items on the deque
    public int size() {
        return count;
    }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) throw new IllegalArgumentException();

        if (count == 0) {
            Node<Item> newNode = new Node<>();
            newNode.item = item;
            newNode.next = last;
            newNode.prev = first;
            first.next = newNode;
            last.prev = newNode;
        } else {
            Node<Item> oldNode = first.next;
            Node<Item> newNode = new Node<>();
            newNode.item = item;
            newNode.next = oldNode;
            oldNode.prev = newNode;
            first.next = newNode;
        }
        count += 1;
    }

    // add the item to the back
    public void addLast(Item item) {
        if (item == null) throw new IllegalArgumentException();

        if (count == 0) {
            Node<Item> newNode = new Node<>();
            newNode.item = item;
            newNode.next = last;
            newNode.prev = first;
            last.prev = newNode;
            first.next = newNode;
        } else {
            Node<Item> oldNode = last.prev;
            Node<Item> newNode = new Node<>();
            newNode.item = item;
            newNode.prev = oldNode;
            oldNode.next = newNode;
            last.prev = newNode;
        }
        count += 1;
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (isEmpty()) throw new NoSuchElementException();

        Node<Item> oldNode = first.next;
        Node<Item> newNode = oldNode.next;
        newNode.prev = first;
        first.next = newNode;

        count -= 1;
        return oldNode.item;
    }

    // remove and return the item from the back
    public Item removeLast() {
        if (isEmpty()) throw new NoSuchElementException();

        Node<Item> oldNode = last.prev;
        Node<Item> newNode = oldNode.prev;
        newNode.next = last;
        last.prev = newNode;

        count -= 1;
        return oldNode.item;
    }

}
