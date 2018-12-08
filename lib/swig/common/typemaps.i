/*
cipher__PubKey* input typemap
*/
%typemap(in) cipher__PubKey* {
	void *argp = 0;
	int res = SWIG_ConvertPtr($input, &argp, SWIGTYPE_p_cipher_PubKey, 0 | 0);
	if (!SWIG_IsOK(res))
		SWIG_exception_fail(SWIG_TypeError, "expecting type PubKey");
	cipher_PubKey* p = (cipher_PubKey*)argp;
	$1 = &p->data;
}


/*
cipher__SecKey* input typemap
*/
%typemap(in) cipher__SecKey*{
	void *argp = 0;
	int res = SWIG_ConvertPtr($input, &argp, SWIGTYPE_p_cipher_SecKey, 0 | 0);
	if (!SWIG_IsOK(res))
		SWIG_exception_fail(SWIG_TypeError, "expecting type SecKey");
	cipher_SecKey* p = (cipher_SecKey*)argp;
	$1 = &p->data;
}

%typemap(in) cipher__Ripemd160* {
	void *argp = 0;
	int res = SWIG_ConvertPtr($input, &argp, SWIGTYPE_p_cipher_Ripemd160, 0 | 0);
	if (!SWIG_IsOK(res))
		SWIG_exception_fail(SWIG_TypeError, "expecting type Ripemd160");
	cipher_Ripemd160* p = (cipher_Ripemd160*)argp;
	$1 = &p->data;
}

%typemap(in) cipher__Sig* {
	void *argp = 0;
	int res = SWIG_ConvertPtr($input, &argp, SWIGTYPE_p_cipher_Sig, 0 | 0);
	if (!SWIG_IsOK(res))
		SWIG_exception_fail(SWIG_TypeError, "expecting type Sig");
	cipher_Sig* p = (cipher_Sig*)argp;
	$1 = &p->data;
}



%typemap(in) cipher__SHA256* {
	void *argp = 0;
	int res = SWIG_ConvertPtr($input, &argp, SWIGTYPE_p_cipher_SHA256, 0 | 0);
	if (!SWIG_IsOK(res))
		SWIG_exception_fail(SWIG_TypeError, "expecting type SHA256");
	cipher_SHA256* p = (cipher_SHA256*)argp;
	$1 = &p->data;
}

%typemap(in) cipher__Checksum* {
	void *argp = 0;
	int res = SWIG_ConvertPtr($input, &argp, SWIGTYPE_p_cipher_Checksum, 0 | 0);
	if (!SWIG_IsOK(res))
		SWIG_exception_fail(SWIG_TypeError, "expecting type Checksum");
	cipher_Checksum* p = (cipher_Checksum*)argp;
	$1 = &p->data;
}

%apply long long  {GoInt_, GoInt};
%apply long int  {ptrdiff_t};
%apply unsigned short  {GoUint16, GoUint16_};
%apply unsigned char  {GoUint8_, GoUint8};
%apply signed char  {GoInt8_, GoInt8};
%apply unsigned long long  {GoUint64, GoUint64_,GoUint_,GoUint};
%apply GoSlice_* {coin__UxArray*};
%apply short {GoInt16_, GoInt16};
%apply int {GoInt32_, Go, GoInt32};
%apply unsigned int {GoUint32_, GoUint32, BOOL, error};
%apply long long  {GoInt64_, GoInt64, GoInt_, GoInt};
%apply float {GoFloat32_, GoFloat32};
%apply double {GoFloat64_, GoFloat64};
%apply long unsigned int {GoUintptr_, GoUintptr}

