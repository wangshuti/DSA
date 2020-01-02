# Leetcode 練習
## 4.Median of Two Sorted Arrays<br>
難度：hard <br>
>There are two sorted arrays nums1 and nums2 of size m and n respectively.<br>
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).<br>
You may assume nums1 and nums2 cannot be both empty.<br>
>>Example:<br>
nums1 = [1, 3]<br>
nums2 = [2]<br>
The median is 2.0<br>
<br>
做下來感覺不像是hard的難度，可能是我投機取巧？<br>
但我寫完後網上搜了下發現大家跟我寫的大同小異<br>
題目是求兩個數組的中位數。我的做法就是將兩個數組合併起來，然後sort。<br>
如果長度是偶數，則中間兩個相加除2，如果是奇數，就直接是中間值。<br>
<br>
## 88.Merge Sorted Array<br>
難度：easy<br>
>Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.<br>
Note:<br>
The number of elements initialized in nums1 and nums2 are m and n respectively.<br>
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.<br>
>>Example:<br>
Input:<br>
nums1 = [1,2,3,0,0,0], m = 3<br>
nums2 = [2,5,6],       n = 3<br>
Output: [1,2,2,3,5,6]<br>
<br>
merge sort的作業寫出來，這題就可以。<br>
跟作業一樣，我運用的是外部空間法。設立一個空的list。原有的兩個list兩兩比較，小的丟進新的list。<br>
最後將所求的nums1等於新的list，就完成了<br>
<br>
## 108.Convert Sorted Array to Binary Search Tree<br>
難度：easy<br>
>Given an array where elements are sorted in ascending order, convert it to a height balanced BST.<br>
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.<br>
>>Example:<br>
Given the sorted array: [-10,-3,0,5,9],<br>
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:<br>
      0<br>
     / \<br>
   -3   9<br>
   /   /<br>
 -10  5<br>
 <br>
這題是將array轉換為BST，BST一直是我頭疼的地方<br>
但因為是已經排序好的array，所以要做的就是就是將array分開，中間點作為root，然後按照BST的結構放好即可<br>
比作業簡單多了~<br>
 <br>
 ## 109.Convert Sorted List to Binary Search Tree <br>
 難度：Medium <br>
 >Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST. <br>
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. <br>
>>Example: <br>
Given the sorted linked list: [-10,-3,0,5,9], <br>
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST: <br>
      0 <br>
     / \ <br>
   -3   9 <br>
   /   / <br>
 -10  5 <br>
  <br>
這題是108的進階版，從array變成了linked list。  <br>
後半部分做法與108一樣。只需前半部分一個個走訪linked list，並將值丟入一個新的array即可。  <br>
<br>
## 902.Sort an Array<br>
難度：Medium<br>
>Given an array of integers nums, sort the array in ascending order.<br>
>>Example 1:<br>
Input: nums = [5,2,3,1]<br>
Output: [1,2,3,5]<br>
<br>
將一個亂序的array sort好。用任何一個學過的sort的演算法都能做到。<br>
在這裡我用的是merge sort。<br>
