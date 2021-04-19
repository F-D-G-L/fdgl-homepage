#!/bin/bash
# SPDX-License-Identifier: GPL-3.0
# vim: set sw=4 ts=4 ex

die() {
	echo "$@"
	exit
}

usage() {
	die "Usage: $(basename $0) [-a author] [-d date ] [-D description] docx"
}


AUTHOR="FIXME"
DATE=$(date +"%d.%m.%Y")
DESCRIPTION="FIXME"

while getopts "a:d:" opts; do
	case $opts in
		a)
			AUTHOR=$OPTARG
			;;
		d)
			DATE=$OPTARG
			;;
		D)
			DESCRIPTION=$OPTARG
			;;
		*)
			usage
			;;
	esac
done

shift "$((OPTIND - 1))"
DOCX=$1
if [ $# -lt 1 ]; then
	usage
fi

which pandoc 2>&1 || die "Please install pandoc to use $(basename $0)"

ARTICLE=${DOCX/.docx/}
MD="$ARTICLE.md"

TEMPDIR=$(mktemp -d $ARTICLE.XXX)

pandoc -f docx -t markdown -o $TEMPDIR/$MD --extract-media $TEMPDIR $DOCX

pushd $TEMPDIR
sed -i "s:$TEMPDIR/media/image:static/img/$ARTICLE:g" $MD
for f in media/*.jpeg; do
	mv $f ${f/image/$ARTICLE};
done
popd

mv $TEMPDIR/media/*.jpeg static/img/
mv $TEMPDIR/$MD pages/

TMP="$(mktemp $ARTICLE.XXX)"
echo "title: $ARTICLE" >> $TMP
echo "date: $DATE" >> $TMP
echo "author: $AUTHOR" >> $TMP
echo "description: $DESCRIPTION" >> $TMP
echo "" >> $TMP 
cat pages/$MD >> $TMP
echo "" >> $TMP 
echo "<hr/>" >> $TMP 
echo "{{ fotogrid([" >> $TMP
for pic in static/img/$ARTICLE*.jpeg; do
	echo "\"$pic\"," >> $TMP;
done
echo "]) | safe }}" >> $TMP
mv $TMP pages/$MD

rm -rf $TEMPDIR
