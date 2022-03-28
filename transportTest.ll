if.else:                                          ; preds = %sw.bb
  store i8 %read_frame.sroa.10.8.extract.trunc, i8* @num_packets
  %conv20 = and i32 %read_frame.sroa.0.0.extract.trunc, 255
  %conv21 = zext i16 %1 to i32
  %2 = trunc i64 %read_frame.sroa.10.8.extract.shift to i32
  