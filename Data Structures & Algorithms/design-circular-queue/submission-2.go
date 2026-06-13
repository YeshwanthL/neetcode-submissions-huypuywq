type Node struct {
    val int
    next *Node
    prev *Node
}

type MyCircularQueue struct {
    space int
    left *Node
    right *Node
}


func Constructor(k int) MyCircularQueue {
    left := &Node{val:0}
    right := &Node{val:0, prev:left}
    left.next = right
    return MyCircularQueue{
        space: k,
        left: left,
        right: right,
    }
}


func (this *MyCircularQueue) EnQueue(value int) bool {
    if this.IsFull(){
        return false
    }
    cur := &Node{val: value, next: this.right, prev: this.right.prev}
    this.right.prev.next = cur
    this.right.prev = cur
    this.space--
    return true
}


func (this *MyCircularQueue) DeQueue() bool {
    if this.IsEmpty(){
        return false
    }
    this.left.next = this.left.next.next
    this.left.next.prev = this.left
    this.space++
    return true
}


func (this *MyCircularQueue) Front() int {
    if this.IsEmpty(){
        return -1
    }
    return this.left.next.val
}


func (this *MyCircularQueue) Rear() int {
    if this.IsEmpty(){
        return -1
    }
    return this.right.prev.val
}


func (this *MyCircularQueue) IsEmpty() bool {
    return this.left.next == this.right
}


func (this *MyCircularQueue) IsFull() bool {
    return this.space == 0
}


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param1 := obj.EnQueue(value);
 * param2 := obj.DeQueue();
 * param3 := obj.Front();
 * param4 := obj.Rear();
 * param5 := obj.IsEmpty();
 * param6 := obj.IsFull();
 */
 