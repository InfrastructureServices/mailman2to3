OUTDIR ?= ${outdir}

ifeq (${OUTDIR}, )
	OUTDIR = ${PWD}
endif

srpm:
	rm -rf .build
	rm -f mailman 
	mkdir mailman && cp -r * mailman || echo "Unable to copy to itself? Ignoring"
	mkdir .build
	tar --exclude-vcs  -hczvf .build/mailman.tgz  mailman
	cp packaging/Fedora/* .build/
	cd .build  && rpmbuild -bs mailman.spec  --define="_sourcedir ${PWD}/.build" --define="_topdir ${PWD}/.build" --define="_srcrpmdir ${OUTDIR}"
	rm -rf mailman .build 

