#!/bin/bash
for i in {1..144}
do
	git add .
	git commit -m 'Push all python projects'
	git push
	sleep 300
done
