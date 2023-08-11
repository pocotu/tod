using System;

class TreeNode
{
    public int Value;
    public TreeNode Left;
    public TreeNode Right;

    public TreeNode(int value)
    {
        Value = value;
        Left = null;
        Right = null;
    }
}

class BinarySearchTree
{
    public TreeNode Root;

    public BinarySearchTree()
    {
        Root = null;
    }

    public void Insert(int value)
    {
        Root = InsertRecursive(Root, value);
    }

    private TreeNode InsertRecursive(TreeNode root, int value)
    {
        if (root == null)
        {
            return new TreeNode(value);
        }

        if (value < root.Value)
        {
            root.Left = InsertRecursive(root.Left, value);
        }
        else if (value > root.Value)
        {
            root.Right = InsertRecursive(root.Right, value);
        }

        return root;
    }

    public bool Search(int value)
    {
        return SearchRecursive(Root, value);
    }

    private bool SearchRecursive(TreeNode root, int value)
    {
        if (root == null)
        {
            return false;
        }

        if (value == root.Value)
        {
            return true;
        }
        else if (value < root.Value)
        {
            return SearchRecursive(root.Left, value);
        }
        else
        {
            return SearchRecursive(root.Right, value);
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        BinarySearchTree tree = new BinarySearchTree();

        tree.Insert(5);
        tree.Insert(3);
        tree.Insert(8);
        tree.Insert(1);
        tree.Insert(4);

        Console.WriteLine(tree.Search(4));  // Output: True
        Console.WriteLine(tree.Search(6));  // Output: False
    }
}
