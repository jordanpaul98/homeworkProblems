HW 8 problem p3 from chapter 5.

need both main.py and DijkstrasShortestPath.py

running it gives this output:

  Step  |       N'      | D(t), p(t) | D(u), p(u) | D(v), p(v) | D(w), p(w) | D(y), p(y) | D(z), p(z) |
  
     0  |   x           |     inf,  |     inf,  |       3, x |       6, x |       6, x |       8, x |
     
     1  |   xv          |       7, v |       6, v |       3, x |       6, x |       6, x |       8, x |
     
     2  |   xvu         |       7, v |       6, v |       3, x |       6, x |       6, x |       8, x |
     
     3  |   xvuw        |       7, v |       6, v |       3, x |       6, x |       6, x |       8, x |
     
     4  |   xvuwy       |       7, v |       6, v |       3, x |       6, x |       6, x |       8, x |
     
     5  |   xvuwyt      |       7, v |       6, v |       3, x |       6, x |       6, x |       8, x |
     
     7  |   xvuwytz     |       7, v |       6, v |       3, x |       6, x |       6, x |       8, x |


  Step  |       N'      | D(v), p(v) | D(w), p(w) | D(x), p(x) | D(y), p(y) | D(z), p(z) |
  
     0  |   u           |       2, u |       5, u |       1, u |      inf,  |      inf,  |
     
     1  |   ux          |       2, u |       4, x |       1, u |       2, x |      inf,  |
     
     2  |   uxy         |       2, u |       3, y |       1, u |       2, x |       4, y |
     
     3  |   uxyv        |       2, u |       3, y |       1, u |       2, x |       4, y |
     
     4  |   uxyvw       |       2, u |       3, y |       1, u |       2, x |       4, y |
     
     6  |   uxyvwz      |       2, u |       3, y |       1, u |       2, x |       4, y |

note: I ran this for a slide problems, which is included with slide() and matches the slides but changing around the starting node seems to give incorrect pathing for some nodes. might be how i'm commparing viewing to previous min pathing
