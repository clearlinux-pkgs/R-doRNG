#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-doRNG
Version  : 1.7.1
Release  : 31
URL      : https://cran.r-project.org/src/contrib/doRNG_1.7.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/doRNG_1.7.1.tar.gz
Summary  : Generic Reproducible Parallel Backend for 'foreach' Loops
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-doMPI
Requires: R-doParallel
Requires: R-foreach
Requires: R-iterators
Requires: R-pkgmaker
Requires: R-rbenchmark
Requires: R-rngtools
BuildRequires : R-doMPI
BuildRequires : R-doParallel
BuildRequires : R-foreach
BuildRequires : R-iterators
BuildRequires : R-pkgmaker
BuildRequires : R-rbenchmark
BuildRequires : R-rngtools
BuildRequires : clr-R-helpers
BuildRequires : texlive

%description
reproducible parallel foreach loops, using independent
    random streams as generated by L'Ecuyer's combined

%prep
%setup -q -c -n doRNG

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531583646

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1531583646
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doRNG
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doRNG
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doRNG
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library doRNG|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/doRNG/DESCRIPTION
/usr/lib64/R/library/doRNG/INDEX
/usr/lib64/R/library/doRNG/Meta/Rd.rds
/usr/lib64/R/library/doRNG/Meta/demo.rds
/usr/lib64/R/library/doRNG/Meta/features.rds
/usr/lib64/R/library/doRNG/Meta/hsearch.rds
/usr/lib64/R/library/doRNG/Meta/links.rds
/usr/lib64/R/library/doRNG/Meta/nsInfo.rds
/usr/lib64/R/library/doRNG/Meta/package.rds
/usr/lib64/R/library/doRNG/Meta/vignette.rds
/usr/lib64/R/library/doRNG/NAMESPACE
/usr/lib64/R/library/doRNG/NEWS
/usr/lib64/R/library/doRNG/R/doRNG
/usr/lib64/R/library/doRNG/R/doRNG.rdb
/usr/lib64/R/library/doRNG/R/doRNG.rdx
/usr/lib64/R/library/doRNG/REFERENCES.bib
/usr/lib64/R/library/doRNG/demo/doRNG.R
/usr/lib64/R/library/doRNG/doc/doRNG.R
/usr/lib64/R/library/doRNG/doc/doRNG.Rnw
/usr/lib64/R/library/doRNG/doc/doRNG.pdf
/usr/lib64/R/library/doRNG/doc/index.html
/usr/lib64/R/library/doRNG/help/AnIndex
/usr/lib64/R/library/doRNG/help/aliases.rds
/usr/lib64/R/library/doRNG/help/doRNG.rdb
/usr/lib64/R/library/doRNG/help/doRNG.rdx
/usr/lib64/R/library/doRNG/help/paths.rds
/usr/lib64/R/library/doRNG/html/00Index.html
/usr/lib64/R/library/doRNG/html/R.css
