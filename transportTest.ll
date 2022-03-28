entry:
  %read_frame.sroa.4122.8.extract.trunc = trunc i64 %read_frame.coerce1 to i8
  %read_frame.sroa.8.8.extract.shift = lshr i64 %read_frame.coerce1, 8
  %read_frame.sroa.8.8.extract.trunc = trunc i64 %read_frame.sroa.8.8.extract.shift to i16
  %read_frame.sroa.10.8.extract.shift = lshr i64 %read_frame.coerce1, 24
  %read_frame.sroa.10.8.extract.trunc = trunc i64 %read_frame.sroa.10.8.extract.shift to i8
  %read_frame.sroa.11.8.extract.shift = lshr i64 %read_frame.coerce1, 32
  %read_frame.sroa.11.8.extract.trunc = trunc i64 %read_frame.sroa.11.8.extract.shift to i8
  %read_frame.sroa.12.8.extract.shift = lshr i64 %read_frame.coerce1, 40
  %read_frame.sroa.12.8.extract.trunc = trunc i64 %read_frame.sroa.12.8.extract.shift to i24
  %conv = trunc i64 %read_frame.coerce0 to i8
  store i8 %conv, i8* @src, align 1, !tbaa !3
  %and2126 = lshr i64 %read_frame.coerce0, 8
  %0 = trunc i64 %and2126 to i8
  %cmp = icmp eq i8 %0, %current_sa
  br i1 %cmp, label %if.then, label %if.end111
  
if.else:                                          ; preds = %sw.bb
  %1 = tail call i16 asm "rorw $$8, ${0:w}", "=r,0,~{cc},~{dirflag},~{fpsr},~{flags}"(i16 %read_frame.sroa.8.8.extract.trunc) #8, !srcloc !6
  store i8 %read_frame.sroa.10.8.extract.trunc, i8* @num_packets, align 1, !tbaa !3
  %conv20 = and i32 %read_frame.sroa.0.0.extract.trunc, 255
  %conv21 = zext i16 %1 to i32
  %2 = trunc i64 %read_frame.sroa.10.8.extract.shift to i32
  %conv22 = and i32 %2, 255
  %call = tail call i32 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([74 x i8], [74 x i8]* @.str, i64 0, i64 0), i32 %conv20, i32 %conv21, i32 %conv22)
  %3 = load i8, i8* @src, align 1, !tbaa !3
  %idxprom.i = zext i8 %3 to i64
  %arrayidx.i = getelementptr inbounds [256 x %struct.ConnectionInfo*], [256 x %struct.ConnectionInfo*]* @connection_infos, i64 0, i64 %idxprom.i
  %4 = load %struct.ConnectionInfo*, %struct.ConnectionInfo** %arrayidx.i, align 8, !tbaa !7
  %cmp.i = icmp eq %struct.ConnectionInfo* %4, null
  br i1 %cmp.i, label %if.end.thread.i, label %if.end.i
  