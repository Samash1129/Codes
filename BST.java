public class BST<T extends Comparable<T>>
{
    Node<T> root;

    public void insert(T key)
    {
        Node<T> newNode = new Node<T>(key);
        Node<T> curr_node = root;
        Node<T> prev_node;

        if (root == null)
        {
            root = newNode;
        }
        else
        {
            while (curr_node != null)
            {
                if(key.compareTo(curr_node.data) < 0)
                {
                    curr_node = curr_node.left;
                    if(curr_node == null)
                    {
                        prev_node = newNode;
                        return;
                    }
                }
                else
                {
                    curr_node = curr_node.right;
                    if(curr_node == null)
                    {
                        prev_node = newNode;
                        return;
                    }
                }
            }
        }
    }

    public void LNR(Node n)
    {
        if (n == null)
        {
            return;
        }
        else
        {
            LNR(n.left);
            System.out.println(n.data);
            LNR(n.right);
        }
    }

    public Node[] find(T key)
    {
        Node<T> curr_node = root;

        while (curr_node != null)
        {
            if (key.compareTo(curr_node.data) == 0)
            {
                return new Node[]{curr_node};
            }
            else if (key.compareTo(curr_node.data) < 0)
            {
                return new Node[]{curr_node.left};
            }
            else if (key.compareTo(curr_node.data) > 0)
            {
                return new Node[]{curr_node.right};
            }
        }
        return null;
    }

    public boolean delete(T key)
    {
        Node[] ref = find(key);

        Node<T> curr_node = ref[1];
        Node<T> prev_node = ref[0];
        boolean isLeftChild = true;

        while(curr_node.data != key)
        {
            prev_node = curr_node;
            if(key.compareTo(curr_node.data) < 0)
            {
                isLeftChild = true;
                curr_node = curr_node.left;
            }
            else
            {
                isLeftChild = false;
                curr_node = curr_node.right;
            }
            if(curr_node == null)
            {
                return false;
            }
        }

        // If no Children (Case 1)
        if(curr_node.left == null && curr_node.right == null)
        {
            if(curr_node == root)
            {
                root = null;
            }
            else if(isLeftChild)
            {
                prev_node.left = null;
            }
            else
            {
                prev_node.right = null;
            }
        }

        // If no right child
        else if(curr_node.right == null)
        {
            if(curr_node == root)
            {
                root = curr_node.left;
            }
            else if(isLeftChild)
            {
                prev_node.left = curr_node.left;
            }
            else
            {
                prev_node.right = curr_node.left;
            }
        }

        // If no left child
        else if(curr_node.left == null)
        {
            if(curr_node == root)
            {
                root = curr_node.right;
            }
            else if(isLeftChild)
            {
                prev_node.left = curr_node.right;
            }
            else
            {
                prev_node.right = curr_node.right;
            }
        }

        // If two child
        else
        {
             Node<T> successor = getSuccessor(curr_node);
             if(curr_node == root)
             {
                 root = successor;
             }
             else if(isLeftChild)
             {
                 prev_node.left = successor;
             }
             else
             {
                 prev_node.right = successor;
             }
             successor.left = curr_node.left;
        }
        return true;
    }

    // When current node doesnt have any child, goes to right child then its left child
    private Node getSuccessor(Node delNode)
    {
        Node<T> prev_successor = delNode;
        Node<T> successor = delNode;
        Node curr_successor = delNode.right;

        while(curr_successor != null)
        {
            prev_successor = successor;
            successor = curr_successor;
            curr_successor = curr_successor.left;
        }
        if(successor != delNode.right)
        {
            prev_successor.left = successor.right;
            successor.right = delNode.right;
        }
        return successor;
    }

    public Node Minimum()
    {
        Node<T> curr_node = root;
        while (curr_node.left != null)
        {
            curr_node = curr_node.left;
        }
        return curr_node;
    }

    public Node Maximum()
    {
        Node<T> curr_node = root;
        while (curr_node.right != null)
        {
            curr_node = curr_node.right;
        }
        return curr_node;
    }

    public static void main(String[] args)
    {
        BST obj = new BST();

        obj.insert(33);
        obj.insert(5);
        obj.insert(6);
        obj.insert(35);
        obj.insert(34);
        obj.insert(40);

        obj.LNR(obj.root);

        System.out.println();

        System.out.println("Found: " + obj.find(40));
        System.out.println("Found: " + obj.find(6));
        System.out.println("Found: " + obj.find(4));

        System.out.println();

        System.out.println("Minimum: " + obj.Minimum().data);
        System.out.println("Maximum: " + obj.Maximum().data);
    }
}
