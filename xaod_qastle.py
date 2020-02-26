function_name = {
    'Jets': ['AntiKt4EMPFlowJets', 'AntiKt4EMTopoJets', 'AntiKt4LCTopoJets'],
    'Tracks': ['CombinedMuonTrackParticles', 'ExtrapolatedMuonTrackParticles', 'GSFTrackParticles',
               'HLT_xAOD__TrackParticleContainer_InDetTrigTrackingxAODCnv_Muon_EFID',
               'InDetForwardTrackParticles', 'InDetTrackParticles',
               'MuonSpectrometerTrackParticles'],
    'Electrons': ['Electrons', 'ForwardElectrons', 'HLT_xAOD__ElectronContainer_egamma_Electrons'],
    'Muons': ['HLT_xAOD__MuonContainer_MuonEFInfo', 'HLT_xAOD__MuonContainer_MuonEFInfo_FullScan',
              'Muons']
}

my_file = open('xaod_branches.txt', 'r')
collections = []
print("(call ResultTTree (call Select (call Select (call EventDataset (list 'localds:bogus')) (lambda (list e) (list")
for line in my_file:
    collection = line.split('.')[0]
    function = ''
    for x in function_name:
        if collection in function_name[x]:
            function = x
            break
    if not collection in collections:
        print("(call (attr e '", function, "') '", collection, "')", sep='')
        collections.append(collection)
print("))) (lambda (list e) (list")

my_file.seek(0)
for line in my_file:
    subscript = collections.index(line.split('.')[0])
    # col_name = line.split('.')[0].lower()[0:3]
    col_name = line.split('.')[0].lower()
    attribute = line.split('.')[1].rstrip()
    print("(call (attr (subscript e ", subscript, ") 'Select') (lambda (list ", col_name,
          ") (call (attr ", col_name, " '", attribute, "'))))", sep='')
print ("))) (list")

my_file.seek(0)
for line in my_file:
    out_name = line.split('.')[0].lower() + '_' + line.split('.')[1].rstrip()
    print("'", out_name, "'", sep='')
print(") 'forkme' 'dude.root')")
