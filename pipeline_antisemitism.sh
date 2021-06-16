echo "STARTING BUILDING PPMI MATRICES"
sh ppmi_antisem.sh
echo "STARTING PROPAGATING"
sh propagate_antisem.sh
echo "CREATING CHART"
python prepare_scores.py
echo "FINISHED"