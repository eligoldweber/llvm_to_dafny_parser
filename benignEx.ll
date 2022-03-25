entry:
  %z = alloca i32, align 4
  %cmp = icmp slt i32 %x, 0
  br i1 %cmp, label %if.then, label %lor.lhs.false

lor.lhs.false:                                    
  %cmp1 = icmp sgt i32 %x, 2
  br i1 %cmp1, label %if.then, label %if.end

if.then:                                          
  br label %return

if.end:                                           
  %add = add nsw i32 %x, 2147483646
  store volatile i32 %add, i32* %z, align 4
  %0 = load volatile i32, i32* %z, align 4
  %cmp2 = icmp ugt i32 %0, 0
  br i1 %cmp2, label %if.then3, label %if.end4

if.then3:
  %cmp2 = icmp ugt i32 %0, 0                                         
  br label %if.end4
  