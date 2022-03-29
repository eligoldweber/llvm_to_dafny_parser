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
  %and2126 = lshr i64 %read_frame.coerce0, 8
  %0 = trunc i64 %and2126 to i8
  %cmp = icmp eq i8 %0, %current_sa
  